from xcp2k.inputsection import InputSection
from xcp2k.classes._print25 import _print25


class _localize1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_iter = None
        self.Max_crazy_angle = None
        self.Crazy_scale = None
        self.Crazy_use_diag = None
        self.Use_history = None
        self.Eps_occupation = None
        self.Out_iter_each = None
        self.Eps_localization = None
        self.Min_or_max = None
        self.Method = None
        self.Jacobi_fallback = None
        self.Jacobi_refinement = None
        self.Restart = None
        self.Lochomo_restart_file_name = None
        self.Loclumo_restart_file_name = None
        self.Operator = None
        self.List = []
        self.List_unoccupied = []
        self.States = None
        self.Energy_range = None
        self.PRINT = _print25()
        self._name = "LOCALIZE"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Max_crazy_angle': 'MAX_CRAZY_ANGLE', 'Crazy_scale': 'CRAZY_SCALE', 'Crazy_use_diag': 'CRAZY_USE_DIAG', 'Use_history': 'USE_HISTORY', 'Eps_occupation': 'EPS_OCCUPATION', 'Out_iter_each': 'OUT_ITER_EACH', 'Eps_localization': 'EPS_LOCALIZATION', 'Min_or_max': 'MIN_OR_MAX', 'Method': 'METHOD', 'Jacobi_fallback': 'JACOBI_FALLBACK', 'Jacobi_refinement': 'JACOBI_REFINEMENT', 'Restart': 'RESTART', 'Lochomo_restart_file_name': 'LOCHOMO_RESTART_FILE_NAME', 'Loclumo_restart_file_name': 'LOCLUMO_RESTART_FILE_NAME', 'Operator': 'OPERATOR', 'States': 'STATES', 'Energy_range': 'ENERGY_RANGE'}
        self._repeated_keywords = {'List': 'LIST', 'List_unoccupied': 'LIST_UNOCCUPIED'}
        self._subsections = {'PRINT': 'PRINT'}
        self._attributes = ['Section_parameters']

