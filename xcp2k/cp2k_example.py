from xcp2k import CP2K
from ase.data import chemical_symbols
import copy

#===============================================================================
#
nele = 84
basis = {}
for i in range(1, nele):
  ele = chemical_symbols[i]
  basis[ele] = 'DZVP-MOLOPT-SR-GTH'
#
for i in [1, 4, 6, 7, 8, 9, 14, 15, 16]:
  ele = chemical_symbols[i]
  basis[ele] = 'DZVP-MOLOPT-GTH'
# print(basis)  
#===============================================================================

#===============================================================================
calc = CP2K()
#===============================================================================
CP2K_INPUT_OT = calc.CP2K_INPUT  # This is the root of the input tree
GLOBAL = CP2K_INPUT_OT.GLOBAL
MOTION = CP2K_INPUT_OT.MOTION
FORCE_EVAL = CP2K_INPUT_OT.FORCE_EVAL_add()
SUBSYS = FORCE_EVAL.SUBSYS
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF
#===============================================================================
GLOBAL.Run_type = "GEO_OPT"  # energy_force, geo_opt, cell_opt
# MOTION.GEO_OPT.Max_force = 1.0E-4

FORCE_EVAL.Method = "Quickstep"
FORCE_EVAL.Stress_tensor = 'ANALYTICAL'
FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"
FORCE_EVAL.PRINT.STRESS_TENSOR.Section_parameters = "ON"

DFT.Basis_set_file_name = "BASIS_MOLOPT"
DFT.Potential_file_name = "POTENTIAL"
#DFT.Charge = 0
#DFT.Multiplicity = 1
#DFT.Uks = True

DFT.MGRID.Ngrids = 5
DFT.MGRID.Cutoff = 800
DFT.MGRID.Rel_cutoff = 60

DFT.XC.XC_FUNCTIONAL.Section_parameters = "PBE"


DFT.QS.Method = 'GPW'
DFT.QS.Eps_default = 1.0E-12
DFT.QS.Map_consistent = True
DFT.QS.Extrapolation = 'ASPC'
DFT.QS.Extrapolation_order = 3

SCF.Scf_guess = "ATOMIC"
SCF.Eps_diis = 0.1
SCF.Eps_scf = 1.0E-6
SCF.Max_scf = 50
SCF.OUTER_SCF.Eps_scf = 1.0E-6
SCF.OUTER_SCF.Max_scf = 20

SCF.OT.Algorithm = 'IRAC'
SCF.OT.Ortho_irac = 'CHOL'
SCF.OT.Eps_irac_switch = 1.0E-4
SCF.OT.Minimizer = "CG"
SCF.OT.N_diis = 7
SCF.OT.Safe_diis = False
SCF.OT.Preconditioner = 'FULL_ALL'
SCF.OT.Energy_gap = 0.05


for i in range(1, nele):
  ele = chemical_symbols[i]
  KIND = SUBSYS.KIND_add('{0}'.format(ele))  # Section_parameters can be provided as argument.
  KIND.Element = '{0}'.format(ele)
  KIND.Basis_set = basis[ele]
  KIND.Potential = 'GTH-PBE' 

#DFT.PRINT.PDOS.Nlumo = 500
#DFT.PRINT.PDOS.EACH.Qs_scf = 0
#DFT.PRINT.PDOS.EACH.Geo_opt = 0
#DFT.PRINT.PDOS.EACH.Md = 0
#DFT.PRINT.PDOS.Add_last = 'NUMERIC'

#DFT.PRINT.MO_CUBES.Nhomo = 30
#DFT.PRINT.MO_CUBES.Nlumo = 30



#===============================================================================
CP2K_INPUT_OT_VDW = copy.deepcopy(CP2K_INPUT_OT)
DFT = CP2K_INPUT_OT_VDW.FORCE_EVAL_list[0].DFT
DFT.XC.VDW_POTENTIAL.Potential_type = 'PAIR_POTENTIAL'
PAIR_POTENTIAL = DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL_add()
PAIR_POTENTIAL.Parameter_file_name = 'dftd3.dat'
PAIR_POTENTIAL.Type = 'DFTD3'
PAIR_POTENTIAL.Reference_functional = 'PBE'
PAIR_POTENTIAL.R_cutoff = '[angstrom] 16'

#===============================================================================
CP2K_INPUT_Diag = copy.deepcopy(CP2K_INPUT_OT)
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF
SCF.Added_mos = 200
SCF.SMEAR.Electronic_temperature = 500
SCF.SMEAR.Method = 'FERMI_DIRAC'
SCF.DIAGONALIZATION.Algorithm = 'STANDARD'
SCF.MIXING.Method = 'BROYDEN_MIXING'
SCF.MIXING.Alpha = 0.1
SCF.MIXING.Beta = 1.5
SCF.MIXING.Nbuffer = 8
