from xcp2k.inputsection import InputSection
from _each189 import _each189


class _current1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Backup_copies = None
        self.Stride = None
        self.EACH = _each189()
        self._name = "CURRENT"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Stride': 'STRIDE', 'Backup_copies': 'BACKUP_COPIES', 'Add_last': 'ADD_LAST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']
