from xcp2k.inputsection import InputSection
from xcp2k.classes._each380 import _each380


class _wannier901(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Seed_name = None
        self.Mp_grid = None
        self.Added_mos = None
        self.Exclude_bands = []
        self.Wannier_functions = []
        self.EACH = _each380()
        self._name = "WANNIER90"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Seed_name': 'SEED_NAME', 'Mp_grid': 'MP_GRID', 'Added_mos': 'ADDED_MOS'}
        self._repeated_keywords = {'Exclude_bands': 'EXCLUDE_BANDS', 'Wannier_functions': 'WANNIER_FUNCTIONS'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Added_bands': 'Added_mos'}
        self._attributes = ['Section_parameters']


    @property
    def Added_bands(self):
        """
        See documentation for Added_mos
        """
        return self.Added_mos

    @Added_bands.setter
    def Added_bands(self, value):
        self.Added_mos = value
