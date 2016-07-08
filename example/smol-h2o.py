#!/usr/bin/env python
from ase import Atom, Atoms
from ase.structure import molecule
from ase.calculators.cp2k import CP2K
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from multiprocessing import Pool
import os
from time import time

atoms = molecule('H2O')
atoms.center(vacuum=5.0)


start = time()
calc = CP2K(label = 'molecules/h2o',
      xc='PBE')
atoms.set_calculator(calc)
gopt = BFGS(atoms, logfile=None)
gopt.run(fmax=1e-2)
end = time()
e = atoms.get_potential_energy()
pos = atoms.get_positions()
d = ((pos[0] - pos[1])**2).sum()**0.5
print('*===============================*')
print('{0:1.4f}  {1:1.4f} '.format( e, d))
print('time = {0}'.format(end - start))
