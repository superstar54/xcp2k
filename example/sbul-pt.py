#!/usr/bin/env python
from xcp2k import CP2K
from ase.atoms import Atom, Atoms
from ase.lattice import bulk
import numpy as np
from multiprocessing import Pool, Process
import os
from ase.eos import EquationOfState


atoms = Atoms([Atom('Pt', (0, 0, 0))])
atoms.pbc = [True, True, True]

datas = []
def run(latt, atoms, datas):
    calc = CP2K(label = 'relax/{0}/pt-relax-{0}'.format(latt, latt),
          xc = 'PBE', 
          cpu = 8,
          cutoff = 500,
          run_type = 'ENERGY_FORCE', 
          atoms = atoms)
    
    atoms.cell=0.5 * latt * np.array([[1.0, 1.0, 0.0],
                                      [0.0, 1.0, 1.0],
                                      [1.0, 0.0, 1.0]])
    atoms = atoms*[2, 2, 2]
    atoms.set_calculator(calc)
    e = atoms.get_potential_energy()
    v = atoms.get_volume()
    datas.append([latt, v, e])
    print('$data {0:1.2f}  {1:1.4f}  {2:1.4f}'.format(latt, v, e))


latts=np.linspace(3.75, 4.00, num=6)
print('------------------------------------------')
print('latt     volume     energy (eV)     bond length (A)')
pool = Pool(processes=10)
for latt in latts:
  pool.apply_async(run, (latt, atoms, datas))
pool.close()
pool.join()


energies = []
volumes = []
f = open('datas/relax.dat')
lines = f.readlines()
for line in lines:
    if line[0:5] == '$data':
      latt, v, e = line.split()[1:4]
      energies.append(float(e))
      volumes.append(float(v))
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(B * 162, 'GPa')
eos.plot('pt-eos.png')

