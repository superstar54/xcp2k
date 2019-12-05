from xcp2k.inputsection import InputSection
from xcp2k.classes._machine_learning1 import _machine_learning1
from xcp2k.classes._print21 import _print21
from xcp2k.classes._line_search5 import _line_search5


class _pao1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_pao = None
        self.Mixing = None
        self.Max_pao = None
        self.Max_cycles = None
        self.Parameterization = None
        self.Regularization = None
        self.Penalty_distance = None
        self.Penalty_strength = None
        self.Precondition = None
        self.Eps_pgf = None
        self.Preopt_dm_file = None
        self.Restart_file = None
        self.Check_gradient_tol = None
        self.Num_gradient_eps = None
        self.Num_gradient_order = None
        self.Check_unitary_tol = None
        self.Linpot_precondition_delta = None
        self.Linpot_initguess_delta = None
        self.Linpot_regularization_delta = None
        self.Linpot_regularization_strength = None
        self.Optimizer = None
        self.Cg_init_steps = None
        self.Cg_reset_limit = None
        self.MACHINE_LEARNING = _machine_learning1()
        self.PRINT_list = []
        self.LINE_SEARCH = _line_search5()
        self._name = "PAO"
        self._keywords = {'Eps_pao': 'EPS_PAO', 'Mixing': 'MIXING', 'Max_pao': 'MAX_PAO', 'Max_cycles': 'MAX_CYCLES', 'Parameterization': 'PARAMETERIZATION', 'Regularization': 'REGULARIZATION', 'Penalty_distance': 'PENALTY_DISTANCE', 'Penalty_strength': 'PENALTY_STRENGTH', 'Precondition': 'PRECONDITION', 'Eps_pgf': 'EPS_PGF', 'Preopt_dm_file': 'PREOPT_DM_FILE', 'Restart_file': 'RESTART_FILE', 'Check_gradient_tol': 'CHECK_GRADIENT_TOL', 'Num_gradient_eps': 'NUM_GRADIENT_EPS', 'Num_gradient_order': 'NUM_GRADIENT_ORDER', 'Check_unitary_tol': 'CHECK_UNITARY_TOL', 'Linpot_precondition_delta': 'LINPOT_PRECONDITION_DELTA', 'Linpot_initguess_delta': 'LINPOT_INITGUESS_DELTA', 'Linpot_regularization_delta': 'LINPOT_REGULARIZATION_DELTA', 'Linpot_regularization_strength': 'LINPOT_REGULARIZATION_STRENGTH', 'Optimizer': 'OPTIMIZER', 'Cg_init_steps': 'CG_INIT_STEPS', 'Cg_reset_limit': 'CG_RESET_LIMIT'}
        self._subsections = {'MACHINE_LEARNING': 'MACHINE_LEARNING', 'LINE_SEARCH': 'LINE_SEARCH'}
        self._repeated_subsections = {'PRINT': '_print21'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print21()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

