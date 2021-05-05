from xcp2k.inputsection import InputSection
from xcp2k.classes._each626 import _each626


class _program_run_info61(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Print_level = None
        self.EACH = _each626()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Print_level': 'PRINT_LEVEL'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Iolevel': 'Print_level'}
        self._attributes = ['Section_parameters']


    @property
    def Iolevel(self):
        """
        See documentation for Print_level
        """
        return self.Print_level

    @Iolevel.setter
    def Iolevel(self, value):
        self.Print_level = value
