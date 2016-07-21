# -*- coding: utf-8 -*-

from cp2k import *
from types import MethodType

calc = CP2K()

def run(self):
    """Monkey patch to submit job through the queue.

    If this is called, then the calculator thinks a job should be run.
    If we are in the queue, we should run it, otherwise, a job should
    be submitted.

    """

    # if we are in the queue and jasp is called or if we want to use
    # mode='run' , we should just run the job. First, we consider how.

    if XCP2KRC['mode'] == 'run':
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


    # if you get here, a job is getting submitted

    jobname = self.prefix
    #print(XCP2KRC['queue.command'])
    #print(XCP2KRC['queue.script'])

    if 'SLURM_CONF' in os.environ:
        cmdlist = ['sbatch']
        cmdlist += ['--job-name', '{0}'.format(jobname)]
        cmdlist += ['--ntasks-per-node', '{0}'.format(self.cpu)]
    elif 'SGE_ROOT' in os.environ:
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
        cmdlist += ['-pe', 'openmpi', '{0}'.format(self.cpu)]
    
    #print(cmdlist)

    p = Popen(cmdlist,
              stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(XCP2KRC['queue.script'])

    #print(out)

    if out == '' or err != '':
        raise Exception('something went wrong in qsub:\n\n{0}'.format(err))

    import time
    #print(out)
    if 'SLURM_CONF' in os.environ:
        job_id = int(out.split()[3])
    elif 'SGE_ROOT' in os.environ:
        job_id = int(out.split()[2])
        

    delay = 0.05
    while True:
        if 'SLURM_CONF' in os.environ:
            output = Popen("sacct -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "COMPLETED" in output[0] and output[0].split()[15]==self.prefix:
                break
            time.sleep(delay)
        elif 'SGE_ROOT' in os.environ:
            output = Popen("qstat -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "do not exist" in output[1]:
                break
            time.sleep(delay)


CP2K.run = MethodType(run, None, CP2K)


def create_cell(self, subsys, atoms):
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
    subsys.CELL.A = A.tolist()
    subsys.CELL.B = B.tolist()
    subsys.CELL.C = C.tolist()

    pbc = atoms.get_pbc()
    periodicity = []
    if pbc[0]:
        periodicity.append("X")
    if pbc[1]:
        periodicity.append("Y")
    if pbc[2]:
        periodicity.append("Z")
    if len(periodicity) == 0:
        subsys.CELL.Periodic = "NONE"
    else:
        subsys.CELL.Periodic = "".join(periodicity)

CP2K.create_cell = MethodType(create_cell, None, CP2K)


def create_coord(self, subsys, atoms, molnames=None):
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
        new_atom = [atom.symbol, atom.position[0], atom.position[1], atom.position[2]]
        if molnames is not None:
            new_atom.append(molnames[i_atom])
        atom_list.append(new_atom)
    subsys.COORD.Default_keyword = atom_list

CP2K.create_coord = MethodType(create_coord, None, CP2K)


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
            fixed_atoms.List = iatom
        
    
    fixed_lists = ''.join('  ' + str(x) for x in sflags_all)
    if len(sflags_all) != 0:
        fixed_atoms = constraint.FIXED_ATOMS_add()
        fixed_atoms.List = fixed_lists

CP2K.create_constraint = MethodType(create_constraint, None, CP2K)


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

CP2K.create_poisson = MethodType(create_poisson, None, CP2K)

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
    self.create_cell(SUBSYS, self.atoms)
    self.create_coord(SUBSYS, self.atoms)
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

CP2K.write_input_file = MethodType(write_input_file, None, CP2K)


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
    

CP2K.pre_write_input_file = MethodType(pre_write_input_file, None, CP2K)


def generate_input(self):
        """Generates a CP2K input file"""
        if len(self.prefix) > 0 and not os.path.exists(self.directory):
            #print('Creating directory: ' + self.directory)
            os.makedirs(self.directory)  # cp2k expects dirs to exist


        # global
        #print('generate intput file')
        root = InputSection('CP2K_INPUT')
        self.params['global']['PROJECT_NAME'] = self.prefix
        for key, value in self.params['global'].items():
            if value is not None:
                root.add_keyword('GLOBAL', '{0}   {1}'.format(key, value))
        

        # force
        for key, value in self.params['forces'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
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
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/MGRID',
                                 '{0}    {1}'.format(key, value))
         
        
        # KPOINTS
        for key, value in self.params['kpoints'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/KPOINTS',
                                 '{0}    {1}'.format(key, value))
        # SCF
        for key, value in self.params['scf'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/SCF',
                                 '{0}    {1}'.format(key, value))

        # smear
        for key, value in self.params['smear'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/SCF/SMEAR',
                                 '{0}    {1}'.format(key, value))
        # DIAGONALIZATION
        for key, value in self.params['dia'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/SCF/DIAGONALIZATION',
                                 '{0}    {1}'.format(key, value))
        # MIXING
        for key, value in self.params['mixing'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/SCF/MIXING',
                                 '{0}    {1}'.format(key, value))
        # OT
        for key, value in self.params['ot'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('FORCE_EVAL/DFT/SCF/OT',
                                 '{0}    {1}'.format(key, value))
        
        # POISSON
        for key, value in self.params['poisson'].items():
            if value is not None and not any(self.atoms.get_pbc()):
                root.add_keyword('FORCE_EVAL/DFT/POISSON',
                                 '{0}    {1}'.format(key, value))
        # MOTION
        for key, value in self.params['geo_opt'].items():
            if value is not None:
                if '/' in key:
                    key = key.split('/')[1]
                root.add_keyword('MOTION/GEO_OPT',
                                 '{0}    {1}'.format(key, value))
        # cell_opt
        if self.ase_params['CELL_OPT'] is not False:
            for key, value in self.params['cell_opt'].items():
                if value is not None:
                    if '/' in key:
                        key = key.split('/')[1]
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
        sflags_all = []
        if self.atoms.constraints:
            for constr in self.atoms.constraints:
                if isinstance(constr, FixScaled):
                    sflags[constr.a] = constr.mask
                elif isinstance(constr, FixAtoms):
                    sflags_all = constr.index
        # this is the same like "kind" module
        subsys = root.get_subsection('MOTION/CONSTRAINT').subsections
        for iatom, atom in enumerate(self.atoms):
            fixed = ''.join([a for a, b in zip('XYZ', sflags[iatom]) if b])
            if len(fixed) != 0:
                s = InputSection(name='FIXED_ATOMS')
                s.keywords.append('{0}  {1}'.format('COMPONENTS_TO_FIX', fixed))
                s.keywords.append('{0}  {1}'.format('LIST', iatom))
                subsys.append(s)
        fixed_atoms = ''.join('  ' + str(x) for x in sflags_all)
        if len(sflags_all) != 0:
                s = InputSection(name='FIXED_ATOMS')
                s.keywords.append('{0}  {1}'.format('LIST', fixed_atoms))
                subsys.append(s)