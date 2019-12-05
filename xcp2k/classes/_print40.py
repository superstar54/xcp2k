from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info26 import _program_run_info26
from xcp2k.classes._restart10 import _restart10
from xcp2k.classes._restart_history4 import _restart_history4
from xcp2k.classes._current2 import _current2


class _print40(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info26()
        self.RESTART = _restart10()
        self.RESTART_HISTORY = _restart_history4()
        self.CURRENT = _current2()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART', 'RESTART_HISTORY': 'RESTART_HISTORY', 'CURRENT': 'CURRENT'}

