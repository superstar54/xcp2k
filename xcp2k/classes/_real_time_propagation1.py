from xcp2k.inputsection import InputSection
from _print32 import _print32


class _real_time_propagation1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_iter = None
        self.Aspc_order = None
        self.Mat_exp = None
        self.Density_propagation = None
        self.Sc_check_start = None
        self.Exp_accuracy = None
        self.Propagator = None
        self.Initial_wfn = None
        self.Apply_delta_pulse = None
        self.Periodic = None
        self.Delta_pulse_direction = None
        self.Delta_pulse_scale = None
        self.Hfx_balance_in_core = None
        self.Orthonormal = None
        self.Mcweeny_max_iter = None
        self.Accuracy_refinement = None
        self.Mcweeny_eps = None
        self.PRINT = _print32()
        self._name = "REAL_TIME_PROPAGATION"
        self._keywords = {'Density_propagation': 'DENSITY_PROPAGATION', 'Hfx_balance_in_core': 'HFX_BALANCE_IN_CORE', 'Aspc_order': 'ASPC_ORDER', 'Apply_delta_pulse': 'APPLY_DELTA_PULSE', 'Delta_pulse_scale': 'DELTA_PULSE_SCALE', 'Delta_pulse_direction': 'DELTA_PULSE_DIRECTION', 'Mcweeny_eps': 'MCWEENY_EPS', 'Max_iter': 'MAX_ITER', 'Mat_exp': 'MAT_EXP', 'Accuracy_refinement': 'ACCURACY_REFINEMENT', 'Eps_iter': 'EPS_ITER', 'Orthonormal': 'ORTHONORMAL', 'Periodic': 'PERIODIC', 'Sc_check_start': 'SC_CHECK_START', 'Initial_wfn': 'INITIAL_WFN', 'Mcweeny_max_iter': 'MCWEENY_MAX_ITER', 'Exp_accuracy': 'EXP_ACCURACY', 'Propagator': 'PROPAGATOR'}
        self._subsections = {'PRINT': 'PRINT'}

