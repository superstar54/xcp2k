from xcp2k.inputsection import InputSection
from _program_run_info37 import _program_run_info37
from _restart12 import _restart12


class _print55(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info37()
        self.RESTART = _restart12()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

