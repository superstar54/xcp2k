from xcp2k.inputsection import InputSection
from _each95 import _each95


class _restart5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Backup_copies = None
        self.Split_restart_file = None
        self.EACH = _each95()
        self._name = "RESTART"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Backup_copies': 'BACKUP_COPIES', 'Add_last': 'ADD_LAST', 'Split_restart_file': 'SPLIT_RESTART_FILE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

