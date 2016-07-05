# -*- coding: utf-8 -*-

# Parameters that can be set to control cp2k calculation. The values which are None, are not written and default parameters of cp2k are used for them.

import os
from ase.units import Rydberg




global_keys = {
'ALLTOALL_SGL': None,
'BLACS_GRID': None,
'BLACS_REPEATABLE': None,
'CALLGRAPH': None,
'CALLGRAPH_FILE_NAME': None,
'ECHO_ALL_HOSTS': None,
'ECHO_INPUT': None,
'ELPA_KERNEL': None,
'EXTENDED_FFT_LENGTHS': None,
'FFTW_PLAN_TYPE': None,
'FFTW_WISDOM_FILE_NAME': None,
'FFT_POOL_SCRATCH_LIMIT': None,
'FLUSH_SHOULD_FLUSH': None,
'OUTPUT_FILE_NAME': None,
'PREFERRED_DIAG_LIBRARY': None,
'PREFERRED_FFT_LIBRARY': None,
'PRINT_LEVEL': None,       # medium
'PROGRAM_NAME': None,
'PROJECT_NAME': None,     # my_system
'RUN_TYPE': 'ENERGY_FORCE',         # md, geo_opt, energy_force
'SAVE_MEM': None,
'SEED': None,
'TRACE': None,
'TRACE_MASTER': None,
'TRACE_MAX': None,
'TRACE_ROUTINES': None,
'WALLTIME': None         # my_cpu_time
}





kpoints_keys = {

'EPS_GEO': None,
'FULL_GRID': None,
'KPOINT': None,
'PARALLEL_GROUP_SIZE': None,
'SCHEME': None,
'SYMMETRY': None,
'VERBOSE': None,
'WAVEFUNCTIONS': None,
}


mgrid_keys = {
'COMMENSURATE': None,
'CUTOFF': 400,
'MULTIGRID_CUTOFF': None,
'MULTIGRID_SET': None,
'NGRIDS': None,
'PROGRESSION_FACTOR': None,
'REALSPACE': None,
'REL_CUTOFF': None,
'SKIP_LOAD_BALANCE_DISTRIBUTED': None,
}

scf_keys = {
'ADDED_MOS': None,
'CHOLESKY': None,
'EPS_DIIS': None,
'EPS_EIGVAL': None,
'EPS_LUMO': None,
'EPS_SCF': 1.00000000E-005,
'EPS_SCF_HISTORY': None,
'LEVEL_SHIFT': None,
'MAX_DIIS': None,
'MAX_ITER_LUMO': None,
'MAX_SCF': 50,
'MAX_SCF_HISTORY': None,
'NCOL_BLOCK': None,
'NROW_BLOCK': None,
'ROKS_F': None,
'ROKS_PARAMETERS': None,
'ROKS_SCHEME': None,
'SCF_GUESS': None,
}

xc_keys = {
'XC_FUNCTIONAL': None,
'XC':'PBE'
}

potential_keys = {
'CONFINEMENT': None,
'POTENTIAL_FILE_NAME': None,
'POTENTIAL_NAME': None,
'PSEUDO_TYPE': None,
}

subsys_keys = {

'CELL': None,
'COLVAR': None,
'COORD': None,
'CORE_COORD': None,
'CORE_VELOCITY': None,
'KIND': None,
'MULTIPOLES': None,
'PRINT': None,
'RNG_INIT': None,
'SHELL_COORD': None,
'SHELL_VELOCITY': None,
'TOPOLOGY': None,
'VELOCITY': None
}

motion_keys = {
'RTYPE': None,       # GEO_OPT, 
'GEO_MINI': None,    # CG, Minimizer algorithm for geometry optimization
'GEO_MAXS': None,    # 10000, Maximum number of geometry optimization steps
'OUT_FORM': None,    # XYZ, Output format
'OUT_UNIT': None,    # angstrom, Output unit
'OUT_STEPS': None,   # Save results every OUT_STEPS steps of geometry optimization
'MD_ENS': None,      # NVT, Thermodynamical ensemble: NVT or NVE
'MD_DT': None,       # 2.0, Integration time step of the Newton’s equation of motion (in fs)
'MD_STEPS': None,    # 10000, Number of MD steps
'MD_TEMP': None,     # 300, Target temperature (in K)
}

restart_keys = {
'RTYPE': None,       # MD
'RESTART': None,     # TRUE
'RESTARTFILE': None, # My_restart_file, Name of the restart file from the previous run
'MD_ENS': None,      # NVT, Thermodynamical ensemble: NVT or NVE
}



#=======================================================================
#CP2K_INPUT / FORCE_EVAL
forces_keys = {
'METHOD': 'Quickstep',
'STRESS_TENSOR': 'ANALYTICAL',
}

#CP2K_INPUT / FORCE_EVAL / PRINT / FORCES
p_forces_keys = {
'FORCES': None,
'SECTION_PARAMETERS': None,
'ADD_LAST': 'No',
'COMMON_ITERATION_LEVELS': None,
'FILENAME': None,
'LOG_PRINT_KEY': None,
'NDIGITS': None,
}

#CP2K_INPUT / FORCE_EVAL / PRINT / STRESS_TENSOR
p_stress_keys = {
'STRESS_TENSOR': None,
'SECTION_PARAMETERS': None,
'ADD_LAST': 'No',
'COMMON_ITERATION_LEVELS': None,
'FILENAME': None,
'LOG_PRINT_KEY': None,
'NDIGITS': None,

}

# CP2K_INPUT / FORCE_EVAL / DFT
dft_keys = {
'BASIS_SET_FILE_NAME': 'BASIS_MOLOPT',
'CHARGE': 0,
'EXCITATIONS': None,
'MULTIPLICITY': None,
'PLUS_U_METHOD': None,
'POTENTIAL_FILE_NAME': 'POTENTIAL',
'RELAX_MULTIPLICITY': None,
'ROKS': None,
'SUBCELLS': None,
'SURFACE_DIPOLE_CORRECTION': None,
'SURF_DIP_DIR': None,
'UKS': True,
'WFN_RESTART_FILE_NAME': None,
}


# CP2K_INPUT / FORCE_EVAL / DFT / POISSON
possion_key = {

'PERIODIC': None,
'POISSON_SOLVER': 'MT',
}

#SUBSYS






#  CP2K_INPUT / FORCE_EVAL / SUBSYS / KIND
kind_key = {

'SECTION_PARAMETERS': None,
'AUX_BASIS_SET': None,
'AUX_FIT_BASIS_SET': None,
'BASIS_SET': 'DZVP-MOLOPT-SR-GTH',
'CORE_CORRECTION': None,
'DFTB3_PARAM': None,
'ELEC_CONF': None,
'ELEMENT': None,
'GHOST': None,
'GPW_TYPE': None,
'HARD_EXP_RADIUS': None,
'KG_POTENTIAL': None,
'LEBEDEV_GRID': None,
'LMAX_DFTB': None,
'LRI_BASIS_SET': None,
'MAO': None,
'MASS': None,
'MAX_RAD_LOCAL': None,
'MM_RADIUS': None,
'NO_OPTIMIZE': None,
'PAO_BASIS_SIZE': None,
'PAO_POTENTIAL_BETA': None,
'PAO_POTENTIAL_MAXL': None,
'PAO_POTENTIAL_NEIGHBORS': None,
'POTENTIAL': 'GTH-' + xc_keys['XC'],
'RADIAL_GRID': None,
'RHO0_EXP_RADIUS': None,
'RI_AUX_BASIS_SET': None,
'SE_P_ORBITALS_ON_H': None,
}


# CP2K_INPUT / FORCE_EVAL / SUBSYS / KIND / DFT_PLUS_U
plus_u_key = {

'SECTION_PARAMETERS': None,
'EPS_U_RAMPING': None,
'INIT_U_RAMPING_EACH_SCF': None,
'L': None,
'U_MINUS_J': None,
'U_RAMPING': None,

}


#===================================================================================
params = {
'global': global_keys,
'kpoints': kpoints_keys,
'mgrid': mgrid_keys,
'scf': scf_keys,
'xc': xc_keys,
'potential': potential_keys,
'subsys': subsys_keys,
'forces': forces_keys,
'p_forces': p_forces_keys,
'p_stress': p_stress_keys,
'dft': dft_keys,
'plus': plus_u_key,
'motion': motion_keys,
'restart': restart_keys,
'possion': possion_key,
'kind': kind_key
}
