from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info50 import _program_run_info50
from xcp2k.classes._restart13 import _restart13


class _print82(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info50()
        self.RESTART = _restart13()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

