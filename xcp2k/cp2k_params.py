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


#=================================================================================
#CP2K_INPUT / MOTION
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

#CP2K_INPUT / MOTION / GEO_OPT
geo_opt_key = {
	
'MAX_DR': None,
'MAX_FORCE': None,
'MAX_ITER': None,
'OPTIMIZER': None,
'RMS_DR': None,
'RMS_FORCE': None,
'STEP_START_VAL': None,
'TYPE': None,

}
#CP2K_INPUT / MOTION / CELL_OPT
cell_opt_key = {
'EXTERNAL_PRESSURE': 0, 
'KEEP_ANGLES': 'True', 
'KEEP_SYMMETRY': None, 
'MAX_DR': None, 
'MAX_FORCE': 0.002, 
'MAX_ITER': 100, 
'OPTIMIZER': 'CG', 
'PRESSURE_TOLERANCE': None, 
'RMS_DR': None, 
'RMS_FORCE': None, 
'STEP_START_VAL': None, 
'TYPE': 'DIRECT_CELL_OPT', 
}


fixedatom_key = {
	
'COMPONENTS_TO_FIX': None,
'EXCLUDE_MM': None,
'EXCLUDE_QM': None,
'LIST': None,
'MM_SUBSYS': None,
'MOLNAME': None,
'QM_SUBSYS': None,

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
'UKS': None,
'WFN_RESTART_FILE_NAME': None,
}

# CP2K_INPUT / FORCE_EVAL / DFT / SCF
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

# CP2K_INPUT / FORCE_EVAL / DFT / SCF / SMEAR
smear_keys = {
	
'SECTION_PARAMETERS': None,
'ELECTRONIC_TEMPERATURE': None,  #300
'EPS_FERMI_DIRAC': None,
'FIXED_MAGNETIC_MOMENT': None,
'LIST': None,
'SME/METHOD': None,    # 'FERMI_DIRAC'
'WINDOW_SIZE': None,

}


# CP2K_INPUT / FORCE_EVAL / DFT / SCF / OT
ot_keys = {

'SECTION_PARAMETERS': None,
'ALGORITHM': None,
'BROYDEN_ADAPTIVE_SIGMA': None,
'BROYDEN_BETA': None,
'BROYDEN_ENABLE_FLIP': None,
'BROYDEN_ETA': None,
'BROYDEN_FORGET_HISTORY': None,
'BROYDEN_GAMMA': None,
'BROYDEN_OMEGA': None,
'BROYDEN_SIGMA': None,
'BROYDEN_SIGMA_DECREASE': None,
'BROYDEN_SIGMA_MIN': None,
'ENERGIES': None,
'ENERGY_GAP': None,
'EPS_IRAC': None,
'EPS_IRAC_FILTER_MATRIX': None,
'EPS_IRAC_QUICK_EXIT': None,
'EPS_IRAC_SWITCH': None,
'EPS_TAYLOR': None,
'GOLD_TARGET': None,
'IRAC_DEGREE': None,
'LINESEARCH': None,
'MAX_IRAC': None,
'MAX_TAYLOR': None,
'MINIMIZER': None,
'MIXED_PRECISION': None,
'NONDIAG_ENERGY': None,
'NONDIAG_ENERGY_STRENGTH': None,
'N_HISTORY_VEC': None,
'OCCUPATION_PRECONDITIONER': None,
'ON_THE_FLY_LOC': None,
'ORTHO_IRAC': None,
'PRECONDITIONER': None,
'PRECOND_SOLVER': None,
'ROTATION': None,
'SAFE_DIIS': None,
'STEPSIZE': None,

}


# CP2K_INPUT / FORCE_EVAL / DFT / SCF / DIAGONALIZATION
diagonalization_keys = {
	
'SECTION_PARAMETERS': None,
'DIA/ALGORITHM': None,
'EPS_ADAPT': None,
'EPS_ITER': None,
'EPS_JACOBI': None,
'JACOBI_THRESHOLD': None,
'MAX_ITER': None,

}
#  CP2K_INPUT / FORCE_EVAL / DFT / SCF / MIXING
mixing_keys = {
	
'SECTION_PARAMETERS': None,
'ALPHA': None,
'BETA': None,
'BROY_W0': None,
'BROY_WMAX': None,
'BROY_WREF': None,
'MAX_GVEC_EXP': None,
'MAX_STEP': None,
'MIX/METHOD': None,
'NBUFFER': None,
'NMIXING': None,
'NSKIP': None,
'N_SIMPLE_MIX': None,
'PULAY_ALPHA': None,
'PULAY_BETA': None,
'REGULARIZATION': None,
'R_FACTOR': None,

}

xc_keys = {
'XC_FUNCTIONAL': None,
'XC':'PBE'
}

#CP2K_INPUT / FORCE_EVAL / DFT / KPOINTS
kpoints_keys = {

'EPS_GEO': None,
'FULL_GRID': None,
'KPOINT': None,
'PARALLEL_GROUP_SIZE': None,
'SCHEME': None,  #'MONKHORST-PACK 5 5 5'
'SYMMETRY': None,
'VERBOSE': None,
'WAVEFUNCTIONS': None,
}


# CP2K_INPUT / FORCE_EVAL / DFT / POISSON
poisson_key = {

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
'potential': potential_keys,
'subsys': subsys_keys,
'forces': forces_keys,
'p_forces': p_forces_keys,
'p_stress': p_stress_keys,
'dft': dft_keys,
'scf': scf_keys,
'smear': smear_keys,
'ot': ot_keys,
'xc': xc_keys,
'dia': diagonalization_keys,
'mixing': mixing_keys,
'kpoints': kpoints_keys,
'mgrid': mgrid_keys,
'plus': plus_u_key,
'motion': motion_keys,
'restart': restart_keys,
'poisson': poisson_key,
'kind': kind_key,
'geo_opt': geo_opt_key,
'cell_opt': cell_opt_key,
}

ase_params = {
'CELL_OPT': False,
'CPU':4,
'NODES':1,
}
