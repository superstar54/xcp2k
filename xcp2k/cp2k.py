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
2) $ASE_CP2K_COMMAND, pointing to the command launching cp2k e.g. 'cp2k.sopt' or 'mpirun -n 4 cp2k.ssmp'. 

For more information about cp2k, please visit:
    http://www.cp2k.org

Author: Xing Wang <xing.wang@psi.ch>
"""


import sys
from subprocess import Popen, PIPE
import os
from os.path import join, isfile, split, islink
import numpy as np
import ase.io
from ase import Atoms, Atom
from ase.calculators.calculator import FileIOCalculator, all_changes, Parameters
from ase.units import Rydberg
from ase.constraints import FixAtoms, FixScaled
from xcp2k.cp2k_tools import *
from scipy.constants import physical_constants, c, h, hbar, e
from xcp2k.classes._CP2K_INPUT1 import _CP2K_INPUT1
from xcp2k.inputparser import CP2KInputParser
import logging
import traceback



config_files = [os.path.join(os.environ['HOME'], '.cp2krc'),
            '.cp2krc']

logger = logging.getLogger('CP2K')
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# logger.setLevel(logging.DEBUG) 

class CP2K(FileIOCalculator):
    """ASE-Calculator for CP2K.

    CP2K is a program to perform atomistic and molecular simulations of solid
    state, liquid, molecular, and biological systems. It provides a general
    framework for different methods such as e.g., density functional theory
    (DFT) using a mixed Gaussian and plane waves approach (GPW) and classical
    pair and many-body potentials.

    CP2K is freely available under the GPL license.
    It is written in Fortran 2003 and can be run efficiently in parallel.

    Check http://www.cp2k.org about how to obtain and install CP2K.
    Make sure that you also have the CP2K-shell available, since it is required
    by the CP2K-calulator.

    Arguments:

    debug: bool
        Flag to enable debug mode. Default is ``False``.
    nodes: int
        Number of nodes used for the calcuation. Default is ``1``.
    env: str
        System of the Cluster.
        Default is ``SLURM``.

    """    
    name = 'cp2k'
    implemented_properties = ['energy', 'energies', 'forces', 'stress', 'charges', 'frequencies']

    def __init__(self, restart=None, mode = 0,  label = './cp2k', ignore_bad_restart_file=False,
                 queue = None, 
                 atoms=None, command=None,
                 debug=False, **kwargs):
        """Construct CP2K-calculator object."""
        # {'nodes': None, 'ntasks-per-node': None, partition': None, 'account': None, 'time': '01:00:00'},
        FileIOCalculator.__init__(self, restart, ignore_bad_restart_file,
                                  label, atoms, **kwargs)
        self.prefix = label.split('/')[-1]
        self.directory = './' + label[0:-len(self.prefix)]
        self.logger = logger
        if debug:
            self.logger.setLevel(debug)
        self.logger.debug('Label: %s'%(self.label))
        self.logger.debug('Directory: %s'%(self.directory))
        self.logger.debug('Prefix: %s'%(self.prefix))
        # Write the file
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.set_queue(queue)
        self.logger = logger
        self.CP2K_INPUT = _CP2K_INPUT1()
        self.out = None
        self.inp = None
        self.symmetry = None
        self.results = {}
        self.parameters = {}  # calculational parameters
        self.atoms = None
        self.positions = None
        if atoms is not None:
            atoms.calc = self
            self.atoms = atoms
            self.natoms = len(atoms)
    def set_queue(self, queue = None):
        command = os.environ.get('ASE_CP2K_COMMAND')
        if queue:
            script = ''
            if 'config' in queue:
                cf = os.path.join(os.environ['HOME'], queue['config'])
                file = open(cf, 'r')
                script = file.read()
                del queue['config']
            else:
                for cf in config_files:
                    if os.path.exists(cf):
                        file = open(cf, 'r')
                        script = file.read()
            with open('%s/.job_file' % self.directory, 'w') as fh:
                fh.writelines("#!/bin/bash\n")
                fh.writelines("#SBATCH --job-name=%s \n" % self.prefix)
                fh.writelines("#SBATCH --output=%s.out\n" % self.prefix)
                fh.writelines("#SBATCH --error=%s.err\n" % self.prefix)
                fh.writelines("#SBATCH --wait\n")
                for key, value in queue.items():
                    if value:
                        fh.writelines("#SBATCH --%s=%s\n" %(key, value))
                fh.writelines('''%s'''% script)
                fh.writelines("%s \n" % command)
            self.command = "sbatch {0}".format('.job_file')
        else:
            self.command = command
        self.logger.debug('Command: %s'%(self.command))

    def update(self, atoms):
        if self.calculation_required(atoms, ['energy']):
            if (self.atoms is None or
                self.atoms.positions.shape != atoms.positions.shape):
                # Completely new calculation just reusing the same
                # calculator, so delete any old cp2k files found.
                self.clean()
            self.calculate(atoms)

    def write(self, label):
        'Write atoms, parameters and calculated results into restart files.'
        self.logger.debug("Writting restart to: ", label)

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

    #
    def update_atoms(self, atoms):
        """read new geometry when ."""
    # Updata atoms positions and cell
        if self.CP2K_INPUT.GLOBAL.Run_type.upper() == 'GEO_OPT':
            xyzfile = join(self.directory, self.prefix+'-pos-1.xyz')
            atoms_sorted = ase.io.read(xyzfile)
            atoms.positions = atoms_sorted.positions
            self.atoms = atoms
        if self.CP2K_INPUT.GLOBAL.Run_type.upper() == 'CELL_OPT':
            xyzfile = join(self.directory, self.prefix+'-pos-1.xyz')
            atoms_sorted = ase.io.read(xyzfile)
            atoms.positions = atoms_sorted.positions
            atoms.cell = self.read_cell()
            self.atoms = atoms
    #
    def read_cell(self,):
        #
        all_cells = []
        # self.read_results()
        n = len(self.outlines)
        for i in range(n):
            if 'CELL| Volume' in self.outlines[i]:
                cell = np.zeros([3, 3])
                for j in range(3):
                    data = self.outlines[i + 1 + j].split()
                    for icell in range(3):
                        cell[j, icell] = float(data[4 + icell])
                all_cells.append(cell)
        self.results['cell'] = cell
        self.results['all_cells'] = np.array(all_cells)
        return cell
    #
    def read_inp(self, inp = None):
        #
        self.CP2K_INPUT = _CP2K_INPUT1()
        if inp is None:
            self.inp = join(self.directory, 'cp2k.inp')
        inputparser = CP2KInputParser()
        inpcalc = inputparser.parse(self, self.inp)
        self.prefix = inpcalc.CP2K_INPUT.GLOBAL.Project_name
        self.natoms = len(inpcalc.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS.COORD.Default_keyword)
        self.inpcalc = inpcalc
        self.constraints = inpcalc.CP2K_INPUT.MOTION.CONSTRAINT
    #
    def read_results(self, out = None):
        self.read_inp()
        # print(self.out)
        if not out:
            self.out = join(self.directory, 'cp2k.out')
        # print('reading results:...', self.out)
        # print(self.out)
        with open(self.out, 'r') as f:
            self.outlines = f.readlines()
        # print(self.outlines[-5:])
        self.read_info()
        converged = self.read_convergence()
        if not converged:
            os.system('tail -5 ' + self.out)
        # raise RuntimeError('CP2K did not converge!\n' +
            #                    'The last lines of output are printed above ' +
            #                    'and should give an indication why.')
        self.read_energy()
        self.read_forces()
        self.read_geometry()
        # self.read_bader_charge()
        # self.read_time()
        self.logger.debug('Read result successfully!')
        #self.read_stress()
    #
    def read_info(self):
        #
        # self.read_results()
        energies = []
        for line in self.outlines:
            if line.rfind('GLOBAL| Project name') > -1:
                self.prefix = line.split()[-1]
            if line.rfind('NUMBER OF NEB REPLICA') > -1:
                self.nimages = int(line.split()[-1])
            if line.rfind('BAND TOTAL ENERGY [au]') > -1:
                e = float(line.split()[-1])
                energies.append(e)
        self.band_total_energies = energies

    def set_results(self, atoms):
        #self.read(atoms)
        self.old_params = self.params.copy()
        self.atoms = atoms.copy()
        self.positions = atoms.positions   # +++++++++++##????
        self.name = 'cp2k'

    def read_convergence(self):
        converged = False
        # self.out = join(self.directory, 'cp2k.out')
        # print('reading results:...', self.out)
        # print(self.out)
        with open(self.out, 'r') as f:
            self.outlines = f.readlines()
        for n, line in enumerate(self.outlines[-100:-1]):
            if line.rfind('PROGRAM ENDED AT') > -1:
                converged = True
                self.logger.debug(line)
            if line.rfind('The number of warnings') > -1:
                data = int(line.split()[9])
                if data>0:
                    self.logger.debug(line)
        return converged


    def read_energy(self):
        energies = []
        free_energies = []
        cone = physical_constants['Hartree energy in eV'][0]
        #
        for line in self.outlines:
            if line.rfind('ENERGY|') > -1:
                E0 = float(line.split()[8])*cone
                energies.append(E0)
                self.results['energy'] = E0

            elif line.rfind('Total energy uncorrected') > -1:
                F = float(line.split()[5])
                free_energies.append(F)
                self.results['free_energy'] = F
        self.results['all_energies'] = energies
        self.results['free_energies'] = free_energies

    def read_atoms(self):
        """Method that reads positions from the output file.

        If 'all' is switched on, the positions for all ionic steps
        in the output file will be returned, in other case only the
        positions for the last ionic configuration are returned."""

        frames = []
        all_positions = []
        # print('positions:')
        for n, line in enumerate(self.outlines):
            if line.rfind('ATOMIC COORDINATES IN angstrom') > -1:
                positions = np.zeros([self.natoms, 3])
                symbols = []
                for iatom in range(self.natoms):
                    data = self.outlines[n + iatom + 4].split()
                    symbols.append(data[2])
                    for ic in range(3):
                        positions[iatom, ic] = float(data[4 + ic])
                atoms = Atoms(symbols = symbols, positions = positions, pbc = [True, True, True])
                all_positions.append(positions)
                frames.append(atoms)
                        # print(float(data[3 + ic])*conf)
        self.results['frames'] = frames
        self.results['all_positions'] = np.array(all_positions)
    def read_forces(self):
        """Method that reads forces from the output file.

        If 'all' is switched on, the forces for all ionic steps
        in the output file will be returned, in other case only the
        forces for the last ionic configuration are returned."""
        conf = physical_constants['atomic unit of force'][0]/physical_constants['electron volt'][0]*10**(-10)
        all_forces = []
        # print('forces:')
        for n, line in enumerate(self.outlines):
            if line.rfind('ATOMIC FORCES in [a.u.]') > -1:
                forces = np.zeros([self.natoms, 3])
                try :
                    for iatom in range(self.natoms):
                        data = self.outlines[n + iatom + 3].split()
                        for iforce in range(3):
                            forces[iatom, iforce] = float(data[3 + iforce])*conf
                    all_forces.append(forces)
                except:
                    print('read forces error, cp2k run may be interupt')
        self.results['forces'] = forces
        self.results['forces0'] = forces.copy()
        self.results['all_forces'] = np.array(all_forces)
    def read_bader_charge(self, filename = None, atoms = None):
        if filename is None:
            filename = join(self.directory, 'ACF.dat')
        if not os.path.exists(filename):
            os.system('bader *cube')
            self.results['bader_charge'] = None
            # return
        if atoms is None:
            atoms = self.results['atoms']
        natoms = len(atoms)
        bader_charge = np.zeros([natoms])
        with open(filename, 'r') as f:
            lines = f.readlines()
        for iatom in range(natoms):
            data = lines[iatom + 2].split()
            bader_charge[iatom] = float(data[4])
        self.results['bader_charge'] = bader_charge

    def read_charges_moments(self):
        """Method that reads charges from the output file.
        """
        
        self.get_number_of_spins()
        self.natoms = len(self.results['atoms'])
        index = 4
        if self.nspin == 2:
            index = 5
        for n, line in enumerate(self.outlines):
            if line.rfind('Mulliken Population Analysis') > -1:
                charges = []
                moments = []
                for iatom in range(self.natoms):
                    data = self.outlines[n + iatom + 3].split()
                    charges.append([iatom, data[1], float(data[index])])
                    if self.nspin == 2:
                        moments.append([iatom, data[1], float(data[index + 1])])
        self.results['charges-M'] = charges
        self.results['moments-M'] = moments
        #
        for n, line in enumerate(self.outlines):
            if line.rfind('Hirshfeld Charges') > -1:
                charges = []
                moments = []
                for iatom in range(self.natoms):
                    data = self.outlines[n + iatom + 3].split()
                    charges.append([iatom, data[1], float(data[index + 1])])
                    if self.nspin == 2:
                        moments.append([iatom, data[1], float(data[index])])
        self.results['charges-H'] = charges
        self.results['moments-H'] = moments


    def read_stress(self):
        
        stress = None
        for n, line in enumerate(self.outlines):
            if (line.rfind('STRESS TENSOR [GPa]') > -1):
                stress = []
                for i in [n + 3, n + 4, n + 5]:
                    data = self.outlines[i].split()
                    stress += [float(data[1]), float(data[2]), float(data[3])]
        # rearrange in 6-component form and return
        self.results['stress'] = np.array([stress[0], stress[4], stress[8],
                                           stress[5], stress[2], stress[1]])
    def read_time(self):

        for n, line in enumerate(self.outlines):
            if (line.rfind('TOTAL TIME') > -1):
                time = float(self.outlines[n + 2].split()[6])
                self.results['time'] = time
    #
    def read_frequency(self):
        frequencies = []
        # print(self.out)
        for line in self.outlines:
            if line.rfind('VIB|Frequency') > -1:
                for f in line.split()[2:]:
                    frequencies.append(float(f))
        self.results['frequencies'] = frequencies


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
            (self.directory != self.old_directory) 
            or (self.params != self.old_params) 
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
        for line in self.outlines:
            if line.find('CP2K| version string') != -1:  # find the first occurence
                version = "CP@K version " + line.split[-1]
                break
        return version
    def get_time(self):
        return self.results['time']

    def create_cell(self, CELL, atoms):
        """Creates the cell for a SUBSYS from an ASE Atoms object.  

        Creates the cell unit vectors and replicates the periodic boundary
        conditions. Notice that this doesn't affect the PBCs used for
        electrostatics! (use create_poisson())  

        args:
            subsys: pycp2k.parsedclasses._subsys1
                The SUBSYS for which the cell is created.
            atoms: ASE Atoms
                The ASE Atoms object from which the cell is extracted.
        """
        cell = atoms.get_cell()
        A = cell[0, :]
        B = cell[1, :]
        C = cell[2, :]
        CELL.A = A.tolist()
        CELL.B = B.tolist()
        CELL.C = C.tolist() 

        pbc = atoms.get_pbc()
        periodicity = []
        if pbc[0]:
            periodicity.append("X")
        if pbc[1]:
            periodicity.append("Y")
        if pbc[2]:
            periodicity.append("Z")
        if len(periodicity) == 0:
            CELL.Periodic = "NONE"
        else:
            CELL.Periodic = "".join(periodicity)
        #
        if 'symmetry' in atoms.info:
            # print('symmetry', atoms.info['symmetry'])
            CELL.Symmetry = atoms.info['symmetry']
    

    def create_coord(self, COORD, atoms, molnames=None, symbol = 'True'):
        """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.    

        args:
            subsys: pycp2k.parsedclasses._subsys1
            The SUBSYS for which the coordinates are created.
            atoms: ASE Atoms
            Atoms from which the coordinates are extracted.
            molnames: list of strings
            The MOLNAME for each atom in correct order
        """
        atom_list = []
        for i_atom, atom in enumerate(atoms):
            if symbol:
                if 'species' in atoms.arrays:
                    new_atom = [atoms.arrays['species'][i_atom], atom.position[0], atom.position[1], atom.position[2]]
                else:
                    new_atom = [atom.symbol, atom.position[0], atom.position[1], atom.position[2]]
            else:
                new_atom = [atom.position[0], atom.position[1], atom.position[2]]
            if molnames is not None:
                new_atom.append(molnames[i_atom])
            atom_list.append(new_atom)
        COORD.Default_keyword = atom_list   

    def create_constraint(self, constraint, atoms, molnames=None):
        """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.    

        args:
            subsys: pycp2k.parsedclasses._subsys1
            The SUBSYS for which the coordinates are created.
            atoms: ASE Atoms
            Atoms from which the coordinates are extracted.
            molnames: list of strings
            The MOLNAME for each atom in correct order
        """
        #write constraint
        if 'cp2k_constraint' in atoms.info:
            if not atoms.info['cp2k_constraint']:
                return
        from ase.constraints import FixAtoms, FixScaled
        self.natoms = len(atoms)
        sflags = np.zeros((self.natoms, 3), dtype=bool)
        sflags_all = []
        if self.atoms.constraints:
            for constr in self.atoms.constraints:
                if isinstance(constr, FixScaled):
                    sflags[constr.a] = constr.mask
                elif isinstance(constr, FixAtoms):
                    sflags_all = sflags_all + constr.index.tolist()
        # this is the same like "kind" module
        for iatom, atom in enumerate(self.atoms):
            fixed = ''.join([a for a, b in zip('XYZ', sflags[iatom]) if b])
            if len(fixed) != 0:
                fixed_atoms = constraint.FIXED_ATOMS_add()
                fixed_atoms.Components_to_fix = fixed
                fixed_atoms.List = iatom + 1
            
        
        fixed_lists = ''.join('  ' + str(x + 1) for x in sflags_all)
        #print(sflags_all)
        if len(sflags_all) != 0:
            fixed_atoms = constraint.FIXED_ATOMS_add()
            fixed_atoms.List = fixed_lists  
    

    def create_poisson(self, poisson, atoms):
        """Creates the periodicity for a POISSON section and tries to guess a
        good solver.    

        args:
            poisson: pycp2k.parsedclasses._poisson1
            The poisson section from DFT or MM for which the periodicity is
            created.
            atoms: ASE Atoms
            The atoms from which the periodicity is extracted.
        """
        # Define periodicity
        pbc = atoms.get_pbc()
        if sum(pbc) == 0:
            poisson.Periodic = "NONE"
        else:
            poisson.Periodic = pbc[0]*"X" + pbc[1]*"Y" + pbc[2]*"Z" 

    def write_input(self, atoms, properties=None, system_changes=None):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT.
        """
        self.pre_write_input_file() 

        SUBSYS = self.CP2K_INPUT.FORCE_EVAL_list[0].SUBSYS
        CONSTRAINT = self.CP2K_INPUT.MOTION.CONSTRAINT
        
        # write atoms
        self.create_cell(SUBSYS.CELL, self.atoms)
        self.create_coord(SUBSYS.COORD, self.atoms)
        self.create_constraint(CONSTRAINT, self.atoms)
        
        # write Kind
        #kinds = dict([(s.Section_parameters, s) for s in SUBSYS.KIND_list])
        #print(kinds)
        #for elem in set(self.atoms.get_chemical_symbols()):
        #    if elem not in kinds.keys():
        #        KIND = SUBSYS.KIND_add(elem)  # Section_parameters can be provided as argument.
        #        KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
        #        KIND.Potential = "GTH-PBE" 

         
        input_contents = self.CP2K_INPUT._print_input(-1)   

        # Write the file
        if len(self.prefix) > 0 and not os.path.exists(self.directory):
                os.makedirs(self.directory)  # cp2k expects dirs to exist
        with open(join(self.directory, 'cp2k.inp'), 'w') as input_file:
            input_file.write(input_contents)    
    

    def pre_write_input_file(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT.
        """
        #self.old_input = self.new_input
        #print("write_input_file")
        GLOBAL = self.CP2K_INPUT.GLOBAL
        FORCE_EVAL = self.CP2K_INPUT.FORCE_EVAL_list[0]
        DFT = FORCE_EVAL.DFT
        SCF = DFT.SCF   

        # project name
        GLOBAL.Project_name = self.prefix
        if GLOBAL.Run_type is None:
            GLOBAL.Run_type = self.params['global']['RUN_TYPE']
        #
        if not FORCE_EVAL.Method:
            FORCE_EVAL.Method = "Quickstep"
        # xc functional 
        #if self.params['xc']['XC'] is not None:
        #    DFT.XC.XC_FUNCTIONAL.Section_parameters = self.params['xc']['XC']
        # forces
        #calc_forces = ['ENERGY_FORCE', 'GEO_OPT', 'CELL_OPT', 'MD']
        #if GLOBAL.Run_type.upper() in calc_forces:
        #    self.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES.Section_parameters = "ON"
            # ***todo
            #self.CP2K_INPUT.FORCE_EVAL_list[0].PRINT.FORCES.Filename = "forces"    

        # basis_set
        #if not DFT.Basis_set_file_name:
        #    DFT.Basis_set_file_name = "BASIS_MOLOPT"
        #if not DFT.Potential_file_name:
        #   DFT.Potential_file_name = "POTENTIAL"
    def get_atomic_kinds(self):
        """Returns number of atomic kind.
        ['O', 'C']

        """ 
        kinds = {}
        
        # print(self.out)
        nk = 0
        for line in self.outlines:
            if line.rfind('Atomic kind:') > -1:
                nk += 1
                kind = line.split()[3]
                na = int(line.split()[-1])
                flag=True
                for k, e in kinds.items():
                    # print(k, e)
                    if e[0]==kind:
                        flag=False
                        kinds[k][1] = na
                if flag:
                    kinds[nk] = [kind, na]
        print(kinds)
        self.kinds = kinds

            
    def get_fermi_level(self):
        """Return the Fermi level."""
        energies = []
        free_energies = []
        cone = physical_constants['Hartree energy in eV'][0]
        #
        
        # print(self.out)
        Ef = 0
        for line in self.outlines:
            if line.rfind('Fermi Energy') > -1 and line.rfind('eV') > -1:
                Ef = float(line.split()[-1])
            if line.rfind('Fermi Energy') > -1 and line.rfind('eV') == -1:
                Ef = float(line.split()[-1])*cone
        self.Ef = Ef
        return Ef
    #
    def read_bandgap(self,):
        """Return the Fermi level."""
        #
        
        # print(self.out)
        bandgap = 10000000
        for line in self.outlines:
            if line.rfind('HOMO - LUMO gap') > -1:
                tempe = float(line.split()[-1])
                if tempe < bandgap:
                    bandgap = tempe
        self.bandgap = bandgap

    def get_number_of_spins(self):
        """Returns number of spins.
        1 if not spin-polarized
        2 if spin-polarized 

        """ 
        self.read_results()
        for line in self.outlines:
            if line.rfind('DFT| Spin') > -1:
                method = line.split()[-1]
                break
        if method=='UKS':
            spin=2
        else:
            spin=1
        self.nspin = spin
        return spin

    def read_geometry(self, prefix = None):
        atoms = None
        if prefix:
            self.prefix = prefix
        self.logger.debug('Read geometry')
        filename1 = self.directory + '/{0}-pos-1.xyz'.format(self.prefix)
        if os.path.isfile(filename1):
            # print(filename1)
            atoms = ase.io.read(filename1)
            atoms.wrap()
            atoms.cell = self.read_cell()
            atoms.pbc = [True, True, True]
            # print(self.constraints.FIXED_ATOMS_list[0].List[0].split())
            constraints = []
            if len(self.constraints.FIXED_ATOMS_list) > 0:
                # print(self.constraints.FIXED_ATOMS_list)
                for List in self.constraints.FIXED_ATOMS_list[0].List:
                    # print(List)
                    if '..' in List:
                        index = List.split('..')
                        List = range(int(index[0]), int(index[1]))
                    else:
                        List = List.split()
                    constraint = FixAtoms(indices = [int(x) -1 for x in List])
                    constraints.append(constraint)
                atoms.set_constraint(constraints)
        # print(atoms)
        if atoms:
            self.results['atoms'] = atoms.copy()
            filename = self.directory + '/{0}.in'.format(self.prefix)
            print('writing to file: ')
            atoms.write(filename)
        else:
            self.results['atoms'] = None
        return atoms
    def get_work_function(self, ax = None, inpfile = 'potential.cube', output = None, shift = False, atoms = None):
        import matplotlib.pyplot as plt
        from ase.io.cube import read_cube_data
        from ase.units import create_units
        from ase.visualize import view
        if ax is None:
            import matplotlib.pyplot as plt
            ax = plt.gca()
        units = create_units('2006')
        #
        filename = os.path.join(self.directory, inpfile)
        data, atoms = read_cube_data(filename)
        # data = data * units['Ry']
        ef = self.get_fermi_level()
        # x, y, z, lp = calc.get_local_potential()
        nx, ny, nz = data.shape
        axy = np.array([np.average(data[:, :, z]) for z in range(nz)])
        # setup the x-axis in realspace
        uc = atoms.get_cell()
        xaxis = np.linspace(0, uc[2][2], nz)
        if shift:
            ax.plot(xaxis, axy - ef)
            ef = 0
        else:
            ax.plot(xaxis, axy)
            ax.plot([min(xaxis), max(xaxis)], [ef, ef], 'k:')
        ax.set_xlabel('Position along z-axis ($\AA$)')
        ax.set_ylabel('Potential (eV)')
        if output:
            plt.savefig('%s'%output)
        # plt.show()
        pos = max(atoms.positions[:, 2])
        ind = (xaxis > pos) & (xaxis < pos + 3)
        # view(atoms)
        # print(xaxis)
        print(pos, ind)
        print(ef)
        wf = np.average(axy[ind]) - ef
        print('min: %s, max: %s'%(pos, pos + 3))
        print('The workfunction is {0:1.2f} eV'.format(wf))
    def read_frames(self):
        """Method that reads forces from the output file.

        If 'all' is switched on, the forces for all ionic steps
        in the output file will be returned, in other case only the
        forces for the last ionic configuration are returned."""
        cone = physical_constants['Hartree energy in eV'][0]
        conf = physical_constants['atomic unit of force'][0]/physical_constants['electron volt'][0]*10**(-10)
        START = 'PROGRAM STARTED AT'
        END = 'PROGRAM ENDED AT'
        indexs = []
        self.read_results()
        n = len(self.outlines)
        for i in range(n):
            index = []
            if START in self.outlines[i]:
                istart = i
            if END in self.outlines[i]:
                indexs.append([istart, i])
        print('nframe: ', len(indexs))
        frames = []
        for index in indexs:
            for i in range(index[0], index[1]):
                line = self.outlines[i]
                if 'CELL| Volume' in line:
                    cell = np.zeros([3, 3])
                    for j in range(3):
                        data = self.outlines[i + 1 + j].split()
                        for icell in range(3):
                            cell[j, icell] = float(data[4 + icell])
                #
                if line.rfind('ENERGY|') > -1:
                    energy = float(line.split()[8])*cone
                # print('positions:')
                if line.rfind('ATOMIC COORDINATES IN angstrom') > -1:
                    positions = np.zeros([self.natoms, 3])
                    symbols = []
                    for iatom in range(self.natoms):
                        data = self.outlines[i + iatom + 4].split()
                        symbols.append(data[2])
                        for ic in range(3):
                            positions[iatom, ic] = float(data[4 + ic])
                #
                if line.rfind('ATOMIC FORCES in [a.u.]') > -1:
                    forces = np.zeros([self.natoms, 3])
                    try :
                        for iatom in range(self.natoms):
                            data = self.outlines[i + iatom + 3].split()
                            for iforce in range(3):
                                forces[iatom, iforce] = float(data[3 + iforce])*conf
                        atoms = Atoms(symbols = symbols, positions = positions, cell = cell, pbc = [True, True, True])
                        calc = CP2K()
                        calc.results['energy'] = energy
                        calc.results['forces'] = forces
                        atoms.calc = calc
                        frames.append(atoms)
                    except:
                        print('read forces error, cp2k run may be interupt')
        self.results['frames'] = frames
    def read_frames_geo(self):
        """Method that reads forces from the output file.

        If 'all' is switched on, the forces for all ionic steps
        in the output file will be returned, in other case only the
        forces for the last ionic configuration are returned."""
        cone = physical_constants['Hartree energy in eV'][0]
        conf = physical_constants['atomic unit of force'][0]/physical_constants['electron volt'][0]*10**(-10)
        self.read_results()
        #
        from ase.io import read
        f = os.path.join(self.directory, '%s-pos-1.xyz'%self.prefix)
        xyzs = read(f, index = ':')
        self.results['xyzs'] = xyzs
        print('n xyz: ', len(xyzs))
        #
        frames = []
        n = 0
        for i in range(len(self.outlines)):
            line = self.outlines[i]
            if 'CELL| Volume' in line:
                cell = np.zeros([3, 3])
                for j in range(3):
                    data = self.outlines[i + 1 + j].split()
                    for icell in range(3):
                        cell[j, icell] = float(data[4 + icell])
            #
            if line.rfind('ENERGY|') > -1:
                energy = float(line.split()[8])*cone
            # print('positions:')
            if line.rfind('ATOMIC COORDINATES IN angstrom') > -1:
                positions = np.zeros([self.natoms, 3])
                symbols = []
                for iatom in range(self.natoms):
                    data = self.outlines[i + iatom + 4].split()
                    symbols.append(data[2])
                    for ic in range(3):
                        positions[iatom, ic] = float(data[4 + ic])
            #
            if n > 0: positions = xyzs[n - 1].positions
            if line.rfind('ATOMIC FORCES in [a.u.]') > -1:
                forces = np.zeros([self.natoms, 3])
                try :
                    for iatom in range(self.natoms):
                        data = self.outlines[i + iatom + 3].split()
                        for iforce in range(3):
                            forces[iatom, iforce] = float(data[3 + iforce])*conf
                    atoms = Atoms(symbols = symbols, positions = positions, cell = cell, pbc = [True, True, True])
                    calc = CP2K()
                    calc.results['energy'] = energy
                    calc.results['forces'] = forces
                    atoms.calc = calc
                    frames.append(atoms)
                    n += 1
                except:
                    print('read forces error, cp2k run may be interupt')
        self.results['frames'] = frames
        print('n frames: ', len(frames))
        
    def to_deepmd(self, label = './', elements = [], compress = False, energy_shift = None):
        # self.read_results()
        # self.read_frames()
        self.results['deepmd'] = {}
        # nframe = len(self.results['frames'])
        all_cells = []
        all_energies = []
        all_positions = []
        all_forces = []
        E0 = 1e10
        for atoms in self.results['frames']:
            E = atoms.calc.results['energy']
            if compress:
                dE = abs(E - E0)
                if dE < compress:
                    continue
            E0 = E
            # print(dE)
            all_energies.append(E)
            all_cells.append(atoms.cell)
            all_positions.append(atoms.positions)
            all_forces.append(atoms.calc.results['forces'])
        nframe = len(all_energies)
        print('nframe: ', nframe)
        all_cells = np.array(all_cells)
        all_energies = np.array(all_energies)
        all_positions = np.array(all_positions)
        all_forces = np.array(all_forces)
        #
        all_cells = all_cells.reshape(nframe, -1)
        all_positions = all_positions.reshape(nframe, -1)
        all_forces = all_forces.reshape(nframe, -1)
        #
        symbols = self.results['frames'][0].get_chemical_symbols()
        if not elements:
            elements = list(set(symbols))
            elements.sort()
        print(elements)
        #
        if energy_shift is not None:
            all_energies = [e - energy_shift for e in all_energies]
        #
        self.results['deepmd']['all_cells'] = all_cells
        self.results['deepmd']['all_energies'] = all_energies
        self.results['deepmd']['all_coords'] = all_positions
        self.results['deepmd']['all_forces'] = all_forces
        self.results['deepmd']['type_map'] = elements
        symbols = np.array([elements.index(x) for x in symbols])
        self.results['deepmd']['type'] = symbols
    def write_deepmd(self, datas, label = './', type_map = False):
        #
        prefix = label.split('/')[-1]
        directory = './' + label[0:-len(prefix)]
        print('save datas to: %s'%label)
        # print(datas)
        if type_map:
            np.savetxt('%s/type_map.raw'%directory, datas['type_map'], fmt = '%s')
        np.save('%s/box.npy'%label, datas['all_cells'])
        np.save('%s/coord.npy'%label, datas['all_coords'])
        np.save('%s/energy.npy'%label, datas['all_energies'])
        np.save('%s/force.npy'%label, datas['all_forces'])
        np.savetxt('%s/type.raw'%directory, datas['type'], fmt = '%d')
        
