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



# Parameters that can be set to control cp2k calculation. The values which are None are not written and default parameters of cp2k are used for them.

float_keys = [
    'aexx',       # Fraction of exact/DFT exchange
]

exp_keys = [
    'ediff',      # stopping-criterion for electronic upd.
    'ediffg',     # stopping-criterion for ionic upd.
    'symprec',    # precession in symmetry routines
    # The next keywords pertain to the VTST add-ons from Graeme Henkelman's
    # group at UT Austin
    'fdstep',     # Finite diference step for IOPT = 1 or 2
]

string_keys = [
    'xc',       # algorithm: Normal (Davidson) | Fast | Very_Fast (RMM-DIIS)
    'gga',        # xc-type: PW PB LM or 91
    'metagga',    #
    'prec',       # Precission of calculation (Low, Normal, Accurate)
    'system',     # name of System
    'tebeg',      #
    'teend',      # temperature during run
    'precfock',    # FFT grid in the HF related routines
]

int_keys = [
    'ialgo',      # algorithm: use only 8 (CG) or 48 (RMM-DIIS)
]

bool_keys = [
    'addgrid',    # finer grid for augmentation charge density
]
list_keys = [
    'dipol',      # center of cell for dipol
]
special_keys = [
    'lreal',      # non-local projectors in real space
]

dict_keys = [
    'ldau_luj',   # dictionary with L(S)DA+U parameters, e.g. {'Fe':{'L':2,
                  # 'U':4.0, 'J':0.9}, ...}
]

keys = [
    # 'NBLOCK' and KBLOCK       inner block; outer block
    # 'NPACO' and APACO         distance and nr. of slots for P.C.
    # 'WEIMIN, EBREAK, DEPER    special control tags
]


class CP2K(Calculator):
    """ASE-Calculator for CP2K.

    """
    name = 'cp2k'

    implemented_properties = ['energy', 'forces', 'stress']
    command = None

    # check data
    if 'CP2K_DATA_DIR' is None:
        pppaths = CP2K_DATA_DIR
    elif 'CP2K_DATA_DIR' in os.environ:
        pppaths = os.environ['CP2K_DATA_DIR']
    else:
        raise RuntimeError('Please set CP2K_DATA_DIR')

    default_parameters = dict(
        run_type='ENERGY_FORCE',
        auto_write=False,
        basis_set='DZVP-MOLOPT-SR-GTH',
        basis_set_file=os.environ['CP2K_DATA_DIR'] + '/BASIS_MOLOPT',
        charge=0,
        cutoff=400 * Rydberg,
        force_eval_method="Quickstep",
        inp='',
        max_scf=50,
        potential_file=os.environ['CP2K_DATA_DIR'] + '/POTENTIAL',
        pseudo_potential='auto',
        forces=True,
        stress_tensor=True,
        uks=False,
        poisson_solver='auto',
        xc='LDA')

    def __init__(self, restart=None, ignore_bad_restart_file=False,
                 label='cp2k', atoms=None, command=None,
                 debug=False, **kwargs):
        """Construct CP2K-calculator object."""

        self._debug = debug
        self._force_env_id = None
        self._shell = None
        self.parameters = None
        self.results = None
        self.label = None
        self.atoms = None
        self.positions = None

        self.directory = split(label)[0]
        self.inp = join(self.directory, 'cp2k.inp')
        self.out = join(self.directory, 'cp2k.out')

        self.initdata()
        self.set(**kwargs)

        # Several places are check to determine self.command
        if command is not None:
            self.command = command
        elif CP2K.command is not None:
            self.command = CP2K.command
        elif 'ASE_CP2K_COMMAND' in os.environ:
            self.command = os.environ['ASE_CP2K_COMMAND']
        else:
            raise RuntimeError('Please set ASE_CP2K_COMMAND')



        Calculator.__init__(self, restart, ignore_bad_restart_file,
                            label, atoms, **kwargs)

        if restart is not None:
            try:
                self.read(restart)
            except:
                if ignore_bad_restart_file:
                    self.reset()
                else:
                    raise

    def initdata(self):         
        self.float_params = {}
        self.exp_params = {}
        self.string_params = {}
        self.int_params = {}
        self.bool_params = {}
        self.list_params = {}
        self.special_params = {}
        self.dict_params = {}
        for key in float_keys:
            self.float_params[key] = None
        for key in exp_keys:
            self.exp_params[key] = None
        for key in string_keys:
            self.string_params[key] = None
        for key in int_keys:
            self.int_params[key] = None
        for key in bool_keys:
            self.bool_params[key] = None
        for key in list_keys:
            self.list_params[key] = None
        for key in special_keys:
            self.special_params[key] = None
        for key in dict_keys:
            self.dict_params[key] = None

        self.input_params = {}


    def set(self, **kwargs):
        """Set parameters like set(key1=value1, key2=value2, ...)."""
        for key in kwargs:
            if key in self.float_params:
                self.float_params[key] = kwargs[key]
            elif key in self.exp_params:
                self.exp_params[key] = kwargs[key]
            elif key in self.string_params:
                self.string_params[key] = kwargs[key]
            elif key in self.int_params:
                self.int_params[key] = kwargs[key]
            elif key in self.bool_params:
                self.bool_params[key] = kwargs[key]
            elif key in self.list_params:
                self.list_params[key] = kwargs[key]
            elif key in self.special_params:
                self.special_params[key] = kwargs[key]
            elif key in self.dict_params:
                self.dict_params[key] = kwargs[key]
            elif key in self.input_params:
                self.input_params[key] = kwargs[key]
            else:
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
        self.parameters.write(label + '_params.ase')
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
        Calculator.calculate(self, atoms, properties, system_changes)

        if self._debug:
            print("system_changes:", system_changes)

        #generate inputfile
        self.generate_input()

        olddir = os.getcwd()
        os.chdir(self.directory)

        self.run()

       # Updata atoms positions and cell
        if self.parameters.run_type == 'geo_opt':
            atoms_sorted = ase.io.read(os.path.split(self.label)[1]+'-pos-1.xyz')
            atoms.positions = atoms_sorted.positions
            atoms.cell = atoms_sorted.cell
        os.chdir(olddir)
        # read results
        self.converged = self.read_convergence()
        self.read_results()
        self.set_results(atoms)
        if self.parameters.auto_write:
            self.write(self.label)
        
    def generate_input(self):
        """Generates a CP2K input file"""
        self.directory = os.path.split(self.label)[0]
        label_dir = self.directory
        if len(label_dir) > 0 and not os.path.exists(label_dir):
            print('Creating directory: ' + label_dir)
            os.makedirs(label_dir)  # cp2k expects dirs to exist


        p = self.parameters
        root = parse_input(p.inp)
        label = os.path.split(self.label)[1]

        root.add_keyword('GLOBAL', 'PROJECT ' + label)
        if p.run_type:
            root.add_keyword('GLOBAL', 'RUN_TYPE ' + p.run_type)
        if p.force_eval_method:
            root.add_keyword('FORCE_EVAL', 'METHOD ' + p.force_eval_method)
        if p.forces:
            root.add_keyword('FORCE_EVAL/PRINT/FORCES',
                             '_SECTION_PARAMETERS_ ON')
        if p.stress_tensor:
            root.add_keyword('FORCE_EVAL', 'STRESS_TENSOR ANALYTICAL')
            root.add_keyword('FORCE_EVAL/PRINT/STRESS_TENSOR',
                             '_SECTION_PARAMETERS_ ON')
        if p.basis_set_file:
            root.add_keyword('FORCE_EVAL/DFT',
                             'BASIS_SET_FILE_NAME ' + p.basis_set_file)
        if p.potential_file:
            root.add_keyword('FORCE_EVAL/DFT',
                             'POTENTIAL_FILE_NAME ' + p.potential_file)
        if p.cutoff:
            root.add_keyword('FORCE_EVAL/DFT/MGRID',
                             'CUTOFF [eV] %.18e' % p.cutoff)
        if p.max_scf:
            root.add_keyword('FORCE_EVAL/DFT/SCF', 'MAX_SCF %d' % p.max_scf)
            root.add_keyword('FORCE_EVAL/DFT/LS_SCF', 'MAX_SCF %d' % p.max_scf)

        if p.xc:
            if p.xc.startswith("XC_"):
                root.add_keyword('FORCE_EVAL/DFT/XC/XC_FUNCTIONAL/LIBXC',
                                 'FUNCTIONAL ' + p.xc)
            else:
                root.add_keyword('FORCE_EVAL/DFT/XC/XC_FUNCTIONAL',
                                 '_SECTION_PARAMETERS_ ' + p.xc)

        if p.uks:
            root.add_keyword('FORCE_EVAL/DFT', 'UNRESTRICTED_KOHN_SHAM ON')

        if p.charge and p.charge != 0:
            root.add_keyword('FORCE_EVAL/DFT', 'CHARGE %d' % p.charge)

        # add Poisson solver if needed
        if p.poisson_solver == 'auto' and not any(self.atoms.get_pbc()):
            root.add_keyword('FORCE_EVAL/DFT/POISSON', 'PERIODIC NONE')
            root.add_keyword('FORCE_EVAL/DFT/POISSON', 'PSOLVER  MT')

        # write coords
        syms = self.atoms.get_chemical_symbols()
        atoms = self.atoms.get_positions()
        for elm, pos in zip(syms, atoms):
            line = '%s %.18e %.18e %.18e' % (elm, pos[0], pos[1], pos[2])
            root.add_keyword('FORCE_EVAL/SUBSYS/COORD', line, unique=False)

        # write cell
        pbc = ''.join([a for a, b in zip('XYZ', self.atoms.get_pbc()) if b])
        if len(pbc) == 0:
            pbc = 'NONE'
        root.add_keyword('FORCE_EVAL/SUBSYS/CELL', 'PERIODIC ' + pbc)
        c = self.atoms.get_cell()
        for i, a in enumerate('ABC'):
            line = '%s %.18e %.18e %.18e' % (a, c[i, 0], c[i, 1], c[i, 2])
            root.add_keyword('FORCE_EVAL/SUBSYS/CELL', line)

        # determine pseudo-potential
        potential = p.pseudo_potential
        if p.pseudo_potential == 'auto':
            if p.xc and p.xc.upper() in ('LDA', 'PADE', 'BP', 'BLYP', 'PBE',):
                potential = 'GTH-' + p.xc.upper()
            else:
                msg = 'No matching pseudo potential found, using GTH-PBE'
                warn(msg, RuntimeWarning)
                potential = 'GTH-PBE'  # fall back

        # write atomic kinds
        subsys = root.get_subsection('FORCE_EVAL/SUBSYS').subsections
        kinds = dict([(s.params, s) for s in subsys if s.name == "KIND"])
        for elem in set(self.atoms.get_chemical_symbols()):
            if elem not in kinds.keys():
                s = InputSection(name='KIND', params=elem)
                subsys.append(s)
                kinds[elem] = s
            if p.basis_set:
                kinds[elem].keywords.append('BASIS_SET ' + p.basis_set)
            if potential:
                kinds[elem].keywords.append('POTENTIAL ' + potential)

        output_lines = ['!!! Generated by ASE !!!'] + root.write()
        inp = open(self.inp, 'w')
        for line in output_lines:
            inp.write(line+'\n')
        inp.close()

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



    def read_results(self):
        converged = self.read_convergence()
        if not converged:
            os.system('tail -20 ' + self.out)
            raise RuntimeError('CP2K did not converge!\n' +
                               'The last lines of output are printed above ' +
                               'and should give an indication why.')
        self.read_energy()
        if self.parameters.forces:
            self.read_forces()
        if self.parameters.forces:
            self.read_stress()
        if ('dipole' in self.parameters.get('output', []) and
            not self.atoms.pbc.any()):
            self.read_dipole()

    def set_results(self, atoms):
        #self.read(atoms)
        self.old_float_params = self.float_params.copy()
        self.old_exp_params = self.exp_params.copy()
        self.old_string_params = self.string_params.copy()
        self.old_int_params = self.int_params.copy()
        self.old_input_params = self.input_params.copy()
        self.old_bool_params = self.bool_params.copy()
        self.old_list_params = self.list_params.copy()
        self.old_dict_params = self.dict_params.copy()
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
            (self.float_params != self.old_float_params) or
            (self.exp_params != self.old_exp_params) or
            (self.string_params != self.old_string_params) or
            (self.int_params != self.old_int_params) or
            (self.bool_params != self.old_bool_params) or
            (self.list_params != self.old_list_params) or
            (self.input_params != self.old_input_params) or
            (self.dict_params != self.old_dict_params)
            or not self.converged):
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






class InputSection(object):
    """Represents a section of a CP2K input file"""
    def __init__(self, name, params=None):
        self.name = name.upper()
        self.params = params
        self.keywords = []
        self.subsections = []

    def write(self):
        """Outputs input section as string"""
        output = []
        for k in self.keywords:
            output.append(k)
        for s in self.subsections:
            if s.params:
                output.append('&%s %s' % (s.name, s.params))
            else:
                output.append('&%s' % s.name)
            for l in s.write():
                output.append('   %s' % l)
            output.append('&END %s' % s.name)
        return output

    def add_keyword(self, path, line, unique=True):
        """Adds a keyword to section."""
        parts = path.upper().split('/', 1)
        candidates = [s for s in self.subsections if s.name == parts[0]]
        if len(candidates) == 0:
            s = InputSection(name=parts[0])
            self.subsections.append(s)
            candidates = [s]
        elif len(candidates) != 1:
            raise Exception('Multiple %s sections found ' % parts[0])

        key = line.split()[0].upper()
        if len(parts) > 1:
            candidates[0].add_keyword(parts[1], line, unique)
        elif key == '_SECTION_PARAMETERS_':
            if candidates[0].params is not None:
                msg = 'Section parameter of section %s already set' % parts[0]
                raise Exception(msg)
            candidates[0].params = line.split(' ', 1)[1].strip()
        else:
            old_keys = [k.split()[0].upper() for k in candidates[0].keywords]
            if unique and key in old_keys:
                msg = 'Keyword %s already present in section %s'
                raise Exception(msg % (key, parts[0]))
            candidates[0].keywords.append(line)

    def get_subsection(self, path):
        """Finds a subsection"""
        parts = path.upper().split('/', 1)
        candidates = [s for s in self.subsections if s.name == parts[0]]
        if len(candidates) > 1:
            raise Exception('Multiple %s sections found ' % parts[0])
        if len(candidates) == 0:
            s = InputSection(name=parts[0])
            self.subsections.append(s)
            candidates = [s]
        if len(parts) == 1:
            return candidates[0]
        return candidates[0].get_subsection(parts[1])


def parse_input(inp):
    """Parses the given CP2K input string"""
    root_section = InputSection('CP2K_INPUT')
    section_stack = [root_section]

    for line in inp.split('\n'):
        line = line.split('!', 1)[0].strip()
        if len(line) == 0:
            continue

        if line.upper().startswith('&END'):
            s = section_stack.pop()
        elif line[0] == '&':
            parts = line.split(' ', 1)
            name = parts[0][1:]
            if len(parts) > 1:
                s = InputSection(name=name, params=parts[1].strip())
            else:
                s = InputSection(name=name)
            section_stack[-1].subsections.append(s)
            section_stack.append(s)
        else:
            section_stack[-1].keywords.append(line)

    return root_section

