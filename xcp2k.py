# -*- coding: utf-8 -*-
from __future__ import print_function

"""This module defines an ASE interface to CP2K.
Developed on the basis of modules by Ole Schuett.  
Two environment flay should be set:
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
from xcp2k_params import *
from xcp2k_tools import *
from xcp2krc import *



class CP2K(Calculator):
    """ASE-Calculator for CP2K.

    """
    name = 'cp2k'

    implemented_properties = ['energy', 'forces', 'stress']



    def __init__(self, restart=None, ignore_bad_restart_file=False,
                 label='cp2k', cpu=4, atoms=None, command=None,
                 debug=False, **kwargs):
        """Construct CP2K-calculator object."""
        #print('Construct CP2K-calculator object.')

        self._debug = debug
        self.results = {}
        self.parameters = {}  # calculational parameters

        self.label = None
        self.directory = None
        self.prefix = None

        #label='dir1/abc': (directory='dir1', prefix='abc')
        self.set_label(label)
        self.inp = join(self.directory, 'cp2k.inp')
        self.out = join(self.directory, 'cp2k.out')

        self.atoms = None
        self.positions = None

        if atoms is not None:
            atoms.calc = self

        self.params = params
        self.ase_params = ase_params
        self.set(**kwargs)
        
        # check data
        if 'CP2K_DATA_DIR' is None:
            pppaths = CP2K_DATA_DIR
        elif 'CP2K_DATA_DIR' in os.environ:
            pppaths = os.environ['CP2K_DATA_DIR']
        else:
            raise RuntimeError('Please set CP2K_DATA_DIR')

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
        self.parameters = Parameters.read(label + '_params.ase')
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
        self.generate_input()

        olddir = os.getcwd()
        os.chdir(self.directory)

        self.run()

       # Updata atoms positions and cell
        if self.params['global']['RUN_TYPE'] == 'GEO_OPT':
            atoms_sorted = ase.io.read(self.prefix+'-pos-1.xyz')
            atoms.positions = atoms_sorted.positions
        if self.params['global']['RUN_TYPE'] == 'CELL_OPT':
            lines = open('cp2k.out', 'r').readlines()
            n = len(lines)
            for i in range(n):
                if 'CELL| Vector' in lines[n - i - 1]:
                    for j in range(3):
                        data = lines[n - i - 1 - j].split()
                        for icell in range(3):
                            atoms.cell[2 - j, icell] = float(data[4 + icell])
                break
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
    
    def generate_input(self):
        """Generates a CP2K input file"""
        if len(self.prefix) > 0 and not os.path.exists(self.directory):
            #print('Creating directory: ' + self.directory)
            os.makedirs(self.directory)  # cp2k expects dirs to exist


        # global
        print('generate intput file')
        root = InputSection('CP2K_INPUT')
        self.params['global']['PROJECT_NAME'] = self.prefix
        for key, value in self.params['global'].items():
            if value is not None:
                root.add_keyword('GLOBAL', '{0}   {1}'.format(key, value))
        

        # force
        for key, value in self.params['forces'].items():
            if value is not None:
                   root.add_keyword('FORCE_EVAL',
                                 '{0}    {1}'.format(key, value))
        
        # print force
        for key, value in self.params['p_forces'].items():
            if value is not None:
                root.add_keyword('FORCE_EVAL/PRINT/FORCES',
                                 '{0}  {1} '.format(key, value))
        # print stress
        for key, value in self.params['p_stress'].items():
            if value is not None:
                root.add_keyword('FORCE_EVAL/PRINT/STRESS_TENSOR',
                                 '{0}  {1} '.format(key, value))
        # XC
        for key, value in self.params['xc'].items():
            if value is not None:
                   root.add_keyword('FORCE_EVAL/DFT/XC/XC_FUNCTIONAL',
                                 '_SECTION_PARAMETERS_ ' + value)
        # BASIS_SET_FILE_NAME
        for key, value in self.params['dft'].items():
            if value is not None:
                root.add_keyword('FORCE_EVAL/DFT',
                                 '{0}    {1}'.format(key, value))

        # MGRID
        for key, value in self.params['mgrid'].items():
            if value is not None:
                root.add_keyword('FORCE_EVAL/DFT/MGRID',
                                 '{0}    {1}'.format(key, value))
        
        # KPOINTS
        for key, value in self.params['kpoints'].items():
            if value is not None:
                root.add_keyword('FORCE_EVAL/DFT/KPOINTS',
                                 '{0}    {1}'.format(key, value))
        # SCF
        for key, value in self.params['scf'].items():
            if value is not None:
                root.add_keyword('FORCE_EVAL/DFT/SCF',
                                 '{0}    {1}'.format(key, value))

        # smear
        # SCF
        for key, value in self.params['smear'].items():
            if value is not None:
                if '0' in key:
                    key = key.split('0')[1]
                root.add_keyword('FORCE_EVAL/DFT/SCF/SMEAR',
                                 '{0}    {1}'.format(key, value))
        # POISSON
        for key, value in self.params['poisson'].items():
            if value is not None and not any(self.atoms.get_pbc()):
                root.add_keyword('FORCE_EVAL/DFT/POISSON',
                                 '{0}    {1}'.format(key, value))
        # MOTION
        for key, value in self.params['geo_opt'].items():
            if value is not None:
                root.add_keyword('MOTION/GEO_OPT',
                                 '{0}    {1}'.format(key, value))
        # cell_opt
        if self.ase_params['CELL_OPT'] is not False:
            for key, value in self.params['cell_opt'].items():
                if value is not None:
                    root.add_keyword('MOTION/CELL_OPT',
                                 '{0}    {1}'.format(key, value))

        self.generate_atoms(root)

        # KIND AND POTENTIAL
        subsys = root.get_subsection('FORCE_EVAL/SUBSYS').subsections
        kinds = dict([(s.params, s) for s in subsys if s.name == "KIND"])
        for elem in set(self.atoms.get_chemical_symbols()):
            if elem not in kinds.keys():
                s = InputSection(name='KIND', params=elem)
                subsys.append(s)
                kinds[elem] = s
                for key, value in self.params['kind'].items():
                    if value is not None:
                        kinds[elem].keywords.append('{0}  {1}'.format(key, value))
        output_lines = ['!!! Generated by ASE !!!'] + root.write()
        inp = open(self.inp, 'w')
        for line in output_lines:
            inp.write(line+'\n')
        inp.close()

    
    def generate_atoms(self, root):
        # SUBSYS
        # write coords
        from ase.constraints import FixAtoms, FixScaled
        syms = self.atoms.get_chemical_symbols()
        positions = self.atoms.get_positions()
        for elm, pos in zip(syms, positions):
            line = '%s  %.20e   %.20e   %.20e' % (elm, pos[0], pos[1], pos[2])
            root.add_keyword('FORCE_EVAL/SUBSYS/COORD', line, unique=False)
        
        # write cell
        pbc = ''.join([a for a, b in zip('XYZ', self.atoms.get_pbc()) if b])
        if len(pbc) == 0:
            pbc = 'NONE'
        root.add_keyword('FORCE_EVAL/SUBSYS/CELL', 'PERIODIC ' + pbc)
        c = self.atoms.get_cell()
        for i, a in enumerate('ABC'):
            line = '%s  %.20e  %.20e  %.20e' % (a, c[i, 0], c[i, 1], c[i, 2])
            root.add_keyword('FORCE_EVAL/SUBSYS/CELL', line)
    
        # write constraint
        sflags = np.zeros((len(self.atoms), 3), dtype=bool)
        if self.atoms.constraints:
            for constr in self.atoms.constraints:
                if isinstance(constr, FixScaled):
                    sflags[constr.a] = constr.mask
                elif isinstance(constr, FixAtoms):
                    sflags[constr.index] = [True, True, True]
        subsys = root.get_subsection('MOTION/CONSTRAINT').subsections
        for iatom, atom in enumerate(self.atoms):
            fixed = ''.join([a for a, b in zip('XYZ', sflags[iatom]) if b])
            if len(fixed) != 0:
                s = InputSection(name='FIXED_ATOMS')
                s.keywords.append('{0}  {1}'.format('COMPONENTS_TO_FIX', fixed))
                s.keywords.append('{0}  {1}'.format('LIST', iatom))
                subsys.append(s)

    def read_results(self):
        converged = self.read_convergence()
        if not converged:
            os.system('tail -20 ' + self.out)
            raise RuntimeError('CP2K did not converge!\n' +
                               'The last lines of output are printed above ' +
                               'and should give an indication why.')
        self.read_energy()
        self.read_forces()
        #self.read_stress()


    def set_results(self, atoms):
        #self.read(atoms)
        self.old_params = self.params.copy()
        self.atoms = atoms.copy()
        self.positions = atoms.positions   # +++++++++++##????
        self.name = 'cp2k'

    def read_convergence(self):
        converged = False
        lines = open(self.out, 'r').readlines()
        for n, line in enumerate(lines):
            if line.rfind('PROGRAM ENDED AT') > -1:
                converged = True
        return converged

    def read_energy(self):
        for line in open(self.out, 'r'):
            if line.rfind('ENERGY|') > -1:
                E0 = float(line.split()[8])
                self.results['energy'] = E0*27.2107

            elif line.rfind('Total energy uncorrected') > -1:
                F = float(line.split()[5])
                self.results['free_energy'] = F

    def read_forces(self):
        """Method that reads forces from the output file.

        If 'all' is switched on, the forces for all ionic steps
        in the output file will be returned, in other case only the
        forces for the last ionic configuration are returned."""
        lines = open(self.out, 'r').readlines()
        forces = np.zeros([len(self.atoms), 3])
        for n, line in enumerate(lines):
            if line.rfind('# Atom   Kind   Element') > -1:
                for iatom in range(len(self.atoms)):
                    data = lines[n + iatom + 1].split()
                    for iforce in range(3):
                        forces[iatom, iforce] = float(data[3 + iforce])*51.421
        self.results['forces'] = forces

    #+++++++++++++++++++++++# unit is not right????
    def read_stress(self):
        lines = open(self.out, 'r').readlines()
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
        for line in open(self.out):
            if line.find('CP2K| version string') != -1:  # find the first occurence
                version = "CP@K version " + line.split[-1]
                break
        return version
    def get_forces(self, atoms):
        self.update(atoms)
        return self.results['forces']

    def get_stress(self, atoms):
        self.update(atoms)
        if self.stress is None:
            raise NotImplementedError
        return self.stress


from xcp2k_extensions import *

