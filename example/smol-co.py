#!/usr/bin/env python
from ase.structure import molecule
from xcp2k import CP2K
from ase.io import read, write
from ase.optimize import BFGS
from ase.vibrations import Vibrations

import os


atoms = molecule('CO')
atoms.center(vacuum=4.0)

atoms.pbc=[True, True, True]

calc = CP2K(label = 'molecules/co',
           cpu = 4, 
           xc='pbe')
atoms.set_calculator(calc)
e = atoms.get_potential_energy()
print('energy: {0:1.4f} '.format(e))
