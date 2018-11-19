from xcp2k.inputsection import InputSection
from _each437 import _each437


class _transmission1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.From_energy = None
        self.Till_energy = None
        self.N_gridpoints = None
        self.EACH = _each437()
        self._name = "TRANSMISSION"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'N_gridpoints': 'N_GRIDPOINTS', 'Till_energy': 'TILL_ENERGY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'From_energy': 'FROM_ENERGY', 'Add_last': 'ADD_LAST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

