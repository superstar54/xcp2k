# -*- coding: utf-8 -*-
from __future__ import print_function

"""This module defines an ASE interface to CP2K.
Developed on the basis of 
1) pycp2k by Singroup 
    https://github.com/SINGROUP/pycp2k
2) ase.calculator.cp2k by Ole Schuett
    https://gitlab.com/ase/ase/blob/master/ase/calculators/cp2k.py
3) jasp by John Kitchin
    https://github.com/jkitchin/jasp

Before running, two environment flay should be set:
1) $CP2K_DATA_DIR, path of the directory containing the basis set files (basis set, pseudo_potential, ...) 
2) $ASE_CP2K_COMMAND, pointing to the command launching cp2k e.g. 'cp2k.sopt' or 'mpirun -n 4 cp2k.ssmp'. Alternatively, user can set the environmental flag, pointing to a python script to exec cp2k, like:

   import os
   exitcode = os.system('cp2k.sopt')

For more information about cp2k, please visit:
    http://www.cp2k.org
Author: Xing Wang <xing.wang@psi.ch>
"""

import ase.io
from ase.calculators.calculator import Calculator, all_changes, Parameters
from ase.units import Rydberg
import os
from os.path import join, isfile, split, islink
from warnings import warn
from subprocess import Popen, PIPE
import numpy as np
from cp2k_params import *
from cp2k_tools import *
from cp2krc import *
#
#from xcp2k.utilities import print_title, print_text, print_warning, print_error
from xcp2k.classes._CP2K_INPUT1 import _CP2K_INPUT1


class CP2K(Calculator):
    """ASE-Calculator for CP2K.
    """
    name = 'cp2k'
    implemented_properties = ['energy', 'forces', 'stress', 'charges']

    def __init__(self, restart=None, mode = 0, ignore_bad_restart_file=False,
                 label='cp2k', cpu = 1, atoms=None, command=None,
                 debug=False, **kwargs):
        """Construct CP2K-calculator object."""

        self.CP2K_INPUT = _CP2K_INPUT1()
        self._debug = debug
        self.mode = mode
        self.label = None
        self.directory = None
        self.prefix = None

        self.symmetry = None

        self.results = {}
        self.parameters = {}  # calculational parameters

        #label='dir1/abc': (directory='dir1', prefix='abc')
        self.set_label(label)
        #self.inp = join(self.directory, 'cp2k.inp')
        #self.out = join(self.directory, 'cp2k.out')

        self.atoms = None
        self.positions = None

        if atoms is not None:
            atoms.calc = self
            self.atoms = atoms

        self.params = params
        self.ase_params = ase_params
        self.set(**kwargs)
        
        # check data
        #if 'CP2K_DATA_DIR' is None:
        #    pppaths = CP2K_DATA_DIR
        #elif 'CP2K_DATA_DIR' in os.environ:
        #    pppaths = os.environ['CP2K_DATA_DIR']
        #else:
        #    raise RuntimeError('Please set CP2K_DATA_DIR')

        # Several places are check to determine self.command
        if command is not None:
            self.command = command
        elif 'ASE_CP2K_COMMAND' in os.environ:
            self.command = os.environ['ASE_CP2K_COMMAND']
        else:
            raise RuntimeError('Please set ASE_CP2K_COMMAND')

        
        if restart is not None:
            try:
                self.read(restart)
            except:
                if ignore_bad_restart_file:
                    self.reset()
                else:
                    raise
        self.cpu = cpu
        #print('Finish construct CP2K-calculator object.')


    def set(self, **kwargs):
        """Set parameters like set(key1=value1, key2=value2, ...)."""
        changed_parameters = {}
        kwargs = capitalize_keys(kwargs)
        for key in kwargs:
            oldvalue = self.parameters.get(key)
            if key not in self.parameters:
                if isinstance(oldvalue, dict):
                # Special treatment for dictionary parameters:
                    for name in value:
                        if name not in oldvalue:
                            raise KeyError(
                                'Unknown subparameter "%s" in '
                                'dictionary parameter "%s"' % (name, key))
                    oldvalue.update(value)
                    value = oldvalue
                changed_parameters[key] = kwargs[key]
                self.parameters[key] = kwargs[key]
            flag = 0
            for param in self.params:
                if key in self.params[param]:
                    self.params[param][key] = kwargs[key]
                    flag = 1
                    break
            if flag ==0 and key in self.ase_params:
                self.ase_params[key] = kwargs[key]
            elif flag ==0 and key not in self.ase_params:
                   raise TypeError('Parameter not defined: ' + key)


    def update(self, atoms):
        if self.calculation_required(atoms, ['energy']):
            if (self.atoms is None or
                self.atoms.positions.shape != atoms.positions.shape):
                # Completely new calculation just reusing the same
                # calculator, so delete any old VASP files found.
                self.clean()
            self.calculate(atoms)

    def write(self, label):
        'Write atoms, parameters and calculated results into restart files.'
        if self._debug:
            print("Writting restart to: ", label)

        self.atoms.write(label + '_restart.traj')
        f = open(label + '_params.ase', 'a')
        for key, val in self.parameters.items():
            f.write('{0} = {1} \n'.format(key, val))
        f.close()
        open(label + '_results.ase', 'w').write(repr(self.results))

    def read(self, label):
        'Read atoms, parameters and calculated results from restart files.'
        self.atoms = ase.io.read(label + '_restart.traj')
        #self.parameters = Parameters.read(label + '_params.ase')
        results_txt = open(label + '_results.ase').read()
        self.results = eval(results_txt, {'array': np.array})

    def calculate(self, atoms=None, properties=None,
                  system_changes=all_changes):
        """Do the calculation."""

        if not properties:
            properties = ['energy']
        
        if self._debug:
            print("system_changes:", system_changes)

        if atoms is not None:
            self.atoms = atoms

        #generate inputfile
        self.write_input_file()
        if self.mode == 1:
            return

        olddir = os.getcwd()
        os.chdir(self.directory)

        self.old_directory = self.directory
        self.run()
        
        # read new geometry
        self.update_atoms(atoms)
       
        # write Jmol
        atoms.write(self.prefix + '.in')

        os.chdir(olddir)
        # read results
        self.converged = self.read_convergence()
        self.read_results()
        self.set_results(atoms)
        self.write(self.directory + '/' + self.prefix)

    def run(self):
        """Method which explicitely runs VASP."""

        if 'ASE_CP2K_COMMAND' in os.environ:
            cp2k = os.environ['ASE_CP2K_COMMAND']
            #print(cp2k)
            exitcode = os.system('%s > %s' % (cp2k, 'cp2k.out'))
        elif 'ASE_CP2K_SCRIPT' in os.environ:
            cp2k = os.environ['ASE_CP2K_SCRIPT']
            locals = {}
            exec(compile(open(cp2k).read(), cp2k, 'exec'), {}, locals)
            exitcode = locals['exitcode']
        else:
            raise RuntimeError('Please set either ASE_CP2K_COMMAND'
                               ' or ASE_CP2K_SCRIPT environment variable')
        if exitcode != 0:
            raise RuntimeError('cp2k exited with exit code: %d.  ' % exitcode)

    def update_atoms(self, atoms):
        """read new geometry when ."""
    # Updata atoms positions and cell
        if self.CP2K_INPUT.GLOBAL.Run_type.upper() == 'GEO_OPT':
            atoms_sorted = ase.io.read(self.prefix+'-pos-1.xyz')
            atoms.positions = atoms_sorted.positions
            self.atoms = atoms
        if self.CP2K_INPUT.GLOBAL.Run_type.upper() == 'CELL_OPT':
            atoms_sorted = ase.io.read(self.prefix+'-pos-1.xyz')
            atoms.positions = atoms_sorted.positions
            lines = open('cp2k.out', 'r').readlines()
            n = len(lines)
            for i in range(n):
                if 'CELL| Volume [angstrom^3]:' in lines[i]:
                    for j in range(3):
                        data = lines[i + 1 + j].split()
                        for icell in range(3):
                            atoms.cell[j, icell] = float(data[4 + icell])
            self.atoms = atoms
            

    def read_results(self):
        converged = self.read_convergence()
        if not converged:
            os.system('tail -20 ' + join(self.directory, 'cp2k.out'))
            raise RuntimeError('CP2K did not converge!\n' +
                               'The last lines of output are printed above ' +
                               'and should give an indication why.')
        self.read_energy()
        self.read_forces()
        #self.read_charges()
        #self.read_fermi()
        #if self.CP2K_INPUT.FORCE_EVAL_list[0].DFT.PRINT.PDOS.
        #self.read_bandgap()
        self.read_time()
        #self.read_stress()


    def set_results(self, atoms):
        #self.read(atoms)
        self.old_params = self.params.copy()
        self.atoms = atoms.copy()
        self.positions = atoms.positions   # +++++++++++##????
        self.name = 'cp2k'

    def read_convergence(self):
        converged = False
        lines = open(join(self.directory, 'cp2k.out'), 'r').readlines()[-100:-1]
        for n, line in enumerate(lines):
            if line.rfind('PROGRAM ENDED AT') > -1:
                converged = True
            if line.rfind('The number of warnings') > -1:
                data = int(line.split()[9])
                if data>0:
                    print(line)
        return converged


    def read_energy(self):
        for line in open(join(self.directory, 'cp2k.out'), 'r'):
            if line.rfind('ENERGY|') > -1:
                E0 = float(line.split()[8])
                self.results['energy'] = E0*27.2113860217

            elif line.rfind('Total energy uncorrected') > -1:
                F = float(line.split()[5])
                self.results['free_energy'] = F

    def read_forces(self):
        """Method that reads forces from the output file.

        If 'all' is switched on, the forces for all ionic steps
        in the output file will be returned, in other case only the
        forces for the last ionic configuration are returned."""
        lines = open(join(self.directory, 'cp2k.out'), 'r').readlines()
        forces = np.zeros([len(self.atoms), 3])
        for n, line in enumerate(lines):
            if line.rfind('# Atom   Kind   Element') > -1:
                for iatom in range(len(self.atoms)):
                    data = lines[n + iatom + 1].split()
                    for iforce in range(3):
                        forces[iatom, iforce] = float(data[3 + iforce])*51.421
        self.results['forces'] = forces

    def read_charges(self):
        """Method that reads charges from the output file.
        """
        lines = open(join(self.directory, 'cp2k.out'), 'r').readlines()
        for n, line in enumerate(lines):
            if line.rfind('Mulliken Population Analysis') > -1:
                charges = []
                for iatom in range(len(self.atoms)):
                    data = lines[n + iatom + 3].split()
                    charges.append([iatom, data[1], float(data[4])])
        self.results['charges'] = charges
        
        for n, line in enumerate(lines):
            if line.rfind('Hirshfeld Charges') > -1:
                charges = []
                for iatom in range(len(self.atoms)):
                    data = lines[n + iatom + 3].split()
                    charges.append([iatom, data[1], float(data[5])])
        self.results['charges'] = charges


    def read_stress(self):
        lines = open(join(self.directory, 'cp2k.out'), 'r').readlines()
        stress = None
        for n, line in enumerate(lines):
            if (line.rfind('STRESS TENSOR [GPa]') > -1):
                stress = []
                for i in [n + 3, n + 4, n + 5]:
                    data = lines[i].split()
                    stress += [float(data[1]), float(data[2]), float(data[3])]
        # rearrange in 6-component form and return
        self.results['stress'] = np.array([stress[0], stress[4], stress[8],
                                           stress[5], stress[2], stress[1]])
    def read_time(self):
        lines = open(join(self.directory, 'cp2k.out'), 'r').readlines()
        for n, line in enumerate(lines):
            if (line.rfind('TOTAL TIME') > -1):
                time = float(lines[n + 2].split()[6])
                self.results['time'] = time

    def clean(self):
        """Method which cleans up after a calculation.

        The default files generated by cp2k will be deleted IF this
        method is called.

        """
        files = ['cp2k.out']
        for f in files:
            try:
                os.remove(f)
            except OSError:
                pass

    def calculation_required(self, atoms, quantities):
        if (self.positions is None or
            (self.atoms != atoms) or
            (self.directory != self.old_directory) or
            (self.params != self.old_params) or not self.converged):
            return True
        return False

    def set_atoms(self, atoms):
        if (atoms != self.atoms):
            self.converged = None
        self.atoms = atoms.copy()

    def get_atoms(self):
        atoms = self.atoms.copy()
        atoms.set_calculator(self)
        return atoms
    def read_version(self):
        version = None
        for line in open(join(self.directory, 'cp2k.out')):
            if line.find('CP2K| version string') != -1:  # find the first occurence
                version = "CP@K version " + line.split[-1]
                break
        return version
    def get_time(self):
        return self.results['time']

    def get_forces(self, atoms):
        self.update(atoms)
        return self.results['forces']

    def get_charges(self, atoms):
        self.update(atoms)
        return self.results['charges']

    def get_stress(self, atoms):
        self.update(atoms)
        if self.stress is None:
            raise NotImplementedError
        return self.stress


from cp2k_extensions import *

