from xcp2k import CP2K
from ase.data import chemical_symbols
import copy

#===============================================================================
calc = CP2K()
#===============================================================================
CP2K_INPUT = calc.CP2K_INPUT  # This is the root of the input tree
GLOBAL = CP2K_INPUT.GLOBAL
MOTION = CP2K_INPUT.MOTION
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
SUBSYS = FORCE_EVAL.SUBSYS
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF
#===============================================================================
GLOBAL.Run_type = "GEO_OPT"  # energy_force, geo_opt, cell_opt

FORCE_EVAL.Method = "Quickstep"
FORCE_EVAL.Stress_tensor = 'ANALYTICAL'
FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"
FORCE_EVAL.PRINT.STRESS_TENSOR.Section_parameters = "ON"

DFT.QS.Method = 'xTB'
DFT.QS.XTB.Do_ewald = True

DFT.POISSON.EWALD.Ewald_type = 'SPME'

SCF.Scf_guess = "MOPAC"
SCF.Eps_diis = 0.1
SCF.Eps_scf = 1.0E-7
SCF.Max_scf = 50
SCF.OUTER_SCF.Eps_scf = 1.0E-6
SCF.OUTER_SCF.Max_scf = 20

SCF.Added_mos = 200
SCF.SMEAR.Electronic_temperature = 500
SCF.SMEAR.Method = 'FERMI_DIRAC'

SCF.DIAGONALIZATION.Algorithm = 'STANDARD'
SCF.MIXING.Method = 'BROYDEN_MIXING'
SCF.MIXING.Alpha = 0.1
SCF.MIXING.Beta = 1.5
SCF.MIXING.Nbuffer = 8


CP2K_INPUT_XTB = copy.deepcopy(CP2K_INPUT)