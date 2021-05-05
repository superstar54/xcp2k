from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info43 import _program_run_info43


class _print66(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info43()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

