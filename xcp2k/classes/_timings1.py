from xcp2k.inputsection import InputSection
from _each2 import _each2


class _timings1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Threshold = None
        self.Sort_by_self_time = None
        self.Report_maxloc = None
        self.Time_mpi = None
        self.Timings_level = None
        self.EACH = _each2()
        self._name = "TIMINGS"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Report_maxloc': 'REPORT_MAXLOC', 'Time_mpi': 'TIME_MPI', 'Sort_by_self_time': 'SORT_BY_SELF_TIME', 'Timings_level': 'TIMINGS_LEVEL', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Threshold': 'THRESHOLD'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

