from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info42 import _program_run_info42
from xcp2k.classes._restart12 import _restart12


class _print64(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info42()
        self.RESTART = _restart12()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}

