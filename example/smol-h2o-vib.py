#!/usr/bin/env python
from ase.structure import molecule
from ase.calculators.cp2k import CP2K
from ase.io import read, write
from ase.optimize import BFGS
from ase.vibrations import Vibrations

import os


atoms = molecule('H2O')
atoms.center(vacuum=6.0)

atoms.pbc=[True, True, True]

calc = CP2K(label = 'molecules/h2o',
           xc='pbe')
atoms.set_calculator(calc)
e = atoms.get_potential_energy()
print('energy: {0:1.4f} '.format(e))
BFGS(atoms).run(fmax=0.001)
pos = atoms.get_positions()
bondlength = sum((pos[1] - pos[0])**2)**0.5
print('bond length = {0} A'.format(bondlength))

vib = Vibrations(atoms)
vib.run()
vib.summary()
