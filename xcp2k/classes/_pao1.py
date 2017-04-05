from xcp2k.inputsection import InputSection
from _print19 import _print19
from _line_search5 import _line_search5


class _pao1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_pao = None
        self.Min_step = None
        self.Mixing = None
        self.Max_pao = None
        self.Max_cycles = None
        self.Max_outer_pao = None
        self.Parameterization = None
        self.Preopt_dm_file = None
        self.Read_restart = None
        self.Check_gradient_param_tol = None
        self.Check_gradient_full_tol = None
        self.Check_unitary_tol = None
        self.Seed = None
        self.Cg_init_steps = None
        self.PRINT_list = []
        self.LINE_SEARCH = _line_search5()
        self._name = "PAO"
        self._keywords = {'Max_pao': 'MAX_PAO', 'Min_step': 'MIN_STEP', 'Preopt_dm_file': 'PREOPT_DM_FILE', 'Eps_pao': 'EPS_PAO', 'Max_outer_pao': 'MAX_OUTER_PAO', 'Cg_init_steps': 'CG_INIT_STEPS', 'Check_unitary_tol': 'CHECK_UNITARY_TOL', 'Max_cycles': 'MAX_CYCLES', 'Seed': 'SEED', 'Read_restart': 'READ_RESTART', 'Parameterization': 'PARAMETERIZATION', 'Mixing': 'MIXING', 'Check_gradient_full_tol': 'CHECK_GRADIENT_FULL_TOL', 'Check_gradient_param_tol': 'CHECK_GRADIENT_PARAM_TOL'}
        self._subsections = {'LINE_SEARCH': 'LINE_SEARCH'}
        self._repeated_subsections = {'PRINT': '_print19'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print19()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

