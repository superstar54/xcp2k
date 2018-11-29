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
from ase.calculators.calculator import Calculator, all_changes, Parameters
from ase.units import Rydberg
from cp2k_params import *
from cp2k_tools import *
from cp2krc import *
from scipy.constants import physical_constants, c, h, hbar, e
from xcp2k.classes._CP2K_INPUT1 import _CP2K_INPUT1
import logging
import traceback

logger = logging.getLogger('CP2K')
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# logger.setLevel(logging.DEBUG) 

class CP2K(Calculator):
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

    def __init__(self, restart=None, mode = 0,  ignore_bad_restart_file=False,
                  env = 'SLURM', ntasks = None, nodes = None, ntasks_per_node = None, time = '1:00:00', atoms=None, command=None,
                 debug=False, **kwargs):
        """Construct CP2K-calculator object."""
        self.xcp2krc = xcp2krc
        self.xcp2krc['env'] = env    # set environment for  job submission
        self.xcp2krc['ntasks'] = ntasks
        self.xcp2krc['nodes'] = nodes
        self.xcp2krc['ntasks-per-node'] = ntasks_per_node

        self.xcp2krc['time'] = time
        if debug:
            logger.setLevel(logging.DEBUG)

        self.CP2K_INPUT = _CP2K_INPUT1()
        self._debug = debug
        self.mode = mode
        self.directory = None
        self.prefix = None
        self.out = None

        self.symmetry = None

        self.results = {}
        self.parameters = {}  # calculational parameters

        self.atoms = None
        self.positions = None

        if atoms is not None:
            atoms.calc = self
            self.atoms = atoms

        self.params = params
        self.ase_params = ase_params
        self.set(**kwargs)
        
        
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
        logger.debug("Writting restart to: ", label)

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
        
        # logger.debug("system_changes:", system_changes)

        if atoms is not None:
            self.atoms = atoms

        #generate inputfile
        logger.debug(os.getcwd())
        self.write_input_file()
        if self.mode == 1:
            return
        cwd = os.getcwd()
        # os.chdir(self.directory)
        self.xcp2krc['script_new'] = self.xcp2krc['script'] + '''
                cd {0}  # this is the current working directory
                cd {1}  # this is the vasp directory
                $ASE_CP2K_COMMAND
            '''.format(cwd, self.directory)
        self.run()
        # os.chdir(cwd)
        self.converged = self.read_convergence()
        # read results
        self.read_results()
        self.set_results(self.atoms)
        # read new geometry
        self.update_atoms(self.atoms)
        # write Jmol
        self.atoms.write(join(self.directory, self.prefix+'.in'))
        self.write(self.directory + '/' + self.prefix)
        


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
            atoms.cell = self.read_cell()
            self.atoms = atoms
    #
    def read_cell(self,):
        #
        cell = np.zeros([3, 3])
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        lines = open(self.out, 'r').readlines()
        n = len(lines)
        for i in range(n):
            if 'CELL| Volume' in lines[i]:
                for j in range(3):
                    data = lines[i + 1 + j].split()
                    for icell in range(3):
                        cell[j, icell] = float(data[4 + icell])
        return cell
            

    def read_results(self):
        converged = self.read_convergence()
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        if not converged:
            os.system('tail -20 ' + self.out)
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
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        lines = open(self.out, 'r').readlines()[-100:-1]
        for n, line in enumerate(lines):
            if line.rfind('PROGRAM ENDED AT') > -1:
                converged = True
            if line.rfind('The number of warnings') > -1:
                data = int(line.split()[9])
                if data>0:
                    print(line)
        return converged


    def read_energy(self):
        energies = []
        free_energies = []
        cone = physical_constants['Hartree energy in eV'][0]
        #
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        # print(self.out)
        for line in open(self.out, 'r'):
            if line.rfind('ENERGY|') > -1:
                E0 = float(line.split()[8])*cone
                energies.append(E0)
                self.results['energy'] = E0

            elif line.rfind('Total energy uncorrected') > -1:
                F = float(line.split()[5])
                free_energies.append(F)
                self.results['free_energy'] = F
        self.results['energies'] = energies
        self.results['free_energies'] = free_energies


    def read_forces(self):
        """Method that reads forces from the output file.

        If 'all' is switched on, the forces for all ionic steps
        in the output file will be returned, in other case only the
        forces for the last ionic configuration are returned."""
        conf = physical_constants['atomic unit of force'][0]/physical_constants['electron volt'][0]*10**(-10)
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        lines = open(self.out, 'r').readlines()
        forces = np.zeros([len(self.atoms), 3])
        for n, line in enumerate(lines):
            if line.rfind('# Atom   Kind   Element') > -1:
                try :
                    for iatom in range(len(self.atoms)):
                        data = lines[n + iatom + 1].split()
                        for iforce in range(3):
                            forces[iatom, iforce] = float(data[3 + iforce])*conf
                except:
                    print('read forces error, cp2k run may be interupt')
        self.results['forces'] = forces

    def read_charges(self):
        """Method that reads charges from the output file.
        """
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        lines = open(self.out, 'r').readlines()
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
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
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
    def read_time(self):
        lines = open(join(self.directory, 'cp2k.out'), 'r').readlines()
        for n, line in enumerate(lines):
            if (line.rfind('TOTAL TIME') > -1):
                time = float(lines[n + 2].split()[6])
                self.results['time'] = time
    #
    def read_frequency(self):
        frequencies = []
        #
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        # print(self.out)
        for line in open(self.out, 'r'):
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


#=======================
    def run(self):
        """Monkey patch to submit job through the queue.    

        If this is called, then the calculator thinks a job should be run.
        If we are in the queue, we should run it, otherwise, a job should
        be submitted.   

        """ 

        # if we are in the queue and jasp is called or if we want to use
        # mode='run' , we should just run the job. First, we consider how.
        logger.debug('run function')
        
        if 'ASE_CP2K_COMMAND' not in os.environ:
            raise RuntimeError('Please set ASE_CP2K_COMMAND in the environment variable')
        # check data
        #if 'CP2K_DATA_DIR' is None:
        #    pppaths = CP2K_DATA_DIR
        #elif 'CP2K_DATA_DIR' in os.environ:
        #    pppaths = os.environ['CP2K_DATA_DIR']
        #else:
        #    raise RuntimeError('Please set CP2K_DATA_DIR')

        #print(os.environ)
        if self.xcp2krc['mode'] == 'run':
            # probably running at cmd line, in serial.
            cp2kcmd = os.environ['ASE_CP2K_COMMAND']
            exitcode = os.system(cp2kcmd)
            return exitcode
        elif 'NHOSTS' in os.environ:
            # we are in the queue. determine if we should run serial
            # or parallel
            #NPROCS = os.environ['NSLOTS ']
            # no question. running in serial.
            cp2kcmd = os.environ['ASE_CP2K_COMMAND']
            #parcmd = 'mpirun -np %i %s' % (NPROCS, cp2kcmd)
            exitcode = os.system(cp2kcmd)
            return exitcode
        elif 'SLURM_JOB_NODELIST' in os.environ:
            # we are in the queue. determine if we should run serial
            # or parallel
            # NPROCS = int(os.environ['SLURM_NTASKS'])
            # no question. running in serial.
            cp2kcmd = os.environ['ASE_CP2K_COMMAND']
            exitcode = os.system(cp2kcmd)
            return exitcode
        elif 'PBS_NODEFILE' in os.environ:
            # we are in the queue. determine if we should run serial
            # or parallel
            # NPROCS = int(os.environ['SLURM_NTASKS'])
            # no question. running in serial.
            cp2kcmd = os.environ['ASE_CP2K_COMMAND']
            exitcode = os.system(cp2kcmd)
            return exitcode 
    

        # if you get here, a job is getting submitted   

        jobname = self.prefix   

        if self.xcp2krc['env'].upper() == 'SLURM':
            cmdlist = ['sbatch']
            cmdlist += ['--wait']
            cmdlist += ['--job-name', '{0}'.format(jobname)]
            if self.xcp2krc['nodes']:
                cmdlist += ['--nodes', '{0}'.format(self.xcp2krc['nodes'])]
            if self.xcp2krc['ntasks']:
                cmdlist += ['--ntasks', '{0}'.format(self.xcp2krc['ntasks'])]
            if self.xcp2krc['ntasks-per-node']:
                cmdlist += ['--ntasks-per-node', '{0}'.format(self.xcp2krc['ntasks-per-node'])]
            cmdlist += ['--time', '{0}'.format(self.xcp2krc['time'])]
            # cmdlist += ['--ntasks-per-node', '{0}'.format(self.cpu)]
        if self.xcp2krc['env'].upper() == 'SGE':
            cmdlist = ['qsub']
            cmdlist += ['-N', '{0}'.format(jobname)]
            cmdlist += ['-pe', 'openmpi', '{0}'.format(self.cpu)]
        if self.xcp2krc['env'].upper() == 'gridview':
            cmdlist = ['qsub']
            cmdlist += ['-N', '{0}'.format(jobname)]
            cmdlist += ['-l', 'nodes=1:ppn={0}'.format(self.cpu)]
            cmdlist += ['-q', 'low']
        
        logger.debug(cmdlist)
        logger.debug(self.xcp2krc['script_new'])    

        try:
            p=Popen(cmdlist, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            out, err = p.communicate(self.xcp2krc['script_new'])
            if out == '' or err != '':
                raise Exception('something went wrong in job queue :\n\n{0}'.format(err))
        except Exception as e:
                print('\n\n something went wrong in job queue.\n\n')
                traceback.print_exc()
                print()
                raise e
        logger.debug(out)
        if self.xcp2krc['env'].upper() == 'SLURM':
            job_id = int(out.split()[3])
        elif self.xcp2krc['env'].upper() == 'SGE':
            job_id = int(out.split()[2])
        elif self.xcp2krc['env'].upper() == 'gridview':
            job_id = int(out.split('.')[0]) 
        logger.debug('jobs_id = ', job_id)
                

        if self.xcp2krc['env'].upper() == 'SLURM':
            output = Popen("sacct -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "COMPLETED" in output[0] and output[0].split()[15]==self.prefix:
                return 
        elif self.xcp2krc['env'].upper() == 'SGE':
            output = Popen("qstat -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "do not exist" in output[1]:
                return 
        elif self.xcp2krc['env'].upper() == 'gridview':
            output = Popen("qstat -R %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "Unknown" in output[1]:
                return 
        # print('jobs failed')    
    

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
        if hasattr(atoms, 'symmetry'):
            CELL.Symmetry = atoms.symmetry  
    

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
        from ase.constraints import FixAtoms, FixScaled
        
        sflags = np.zeros((len(self.atoms), 3), dtype=bool)
        sflags_all = []
        if self.atoms.constraints:
            for constr in self.atoms.constraints:
                if isinstance(constr, FixScaled):
                    sflags[constr.a] = constr.mask
                elif isinstance(constr, FixAtoms):
                    sflags_all = constr.index
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

    def write_input_file(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT.
        """
        #self.old_input = self.new_input
        #print("write_input_file")
        
        
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
            