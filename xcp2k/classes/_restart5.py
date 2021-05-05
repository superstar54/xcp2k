from xcp2k.inputsection import InputSection
from xcp2k.classes._each96 import _each96


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
        self.EACH = _each96()
        self._name = "RESTART"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Backup_copies': 'BACKUP_COPIES', 'Split_restart_file': 'SPLIT_RESTART_FILE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

