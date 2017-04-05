from xcp2k.inputsection import InputSection
from _program_run_info23 import _program_run_info23
from _restart10 import _restart10
from _restart_history4 import _restart_history4
from _current1 import _current1


class _print32(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info23()
        self.RESTART = _restart10()
        self.RESTART_HISTORY = _restart_history4()
        self.CURRENT = _current1()
        self._name = "PRINT"
        self._subsections = {'CURRENT': 'CURRENT', 'RESTART_HISTORY': 'RESTART_HISTORY', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

