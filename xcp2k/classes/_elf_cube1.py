from xcp2k.inputsection import InputSection
from xcp2k.classes._each262 import _each262


class _elf_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Append = None
        self.Density_cutoff = None
        self.EACH = _each262()
        self._name = "ELF_CUBE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Append': 'APPEND', 'Density_cutoff': 'DENSITY_CUTOFF'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

