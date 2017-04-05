from xcp2k.inputsection import InputSection
from _program_run_info31 import _program_run_info31
from _restart11 import _restart11


class _print40(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info31()
        self.RESTART = _restart11()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

