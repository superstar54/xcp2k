from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info4 import _program_run_info4
from xcp2k.classes._rotational_info1 import _rotational_info1


class _print2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info4()
        self.ROTATIONAL_INFO = _rotational_info1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'ROTATIONAL_INFO': 'ROTATIONAL_INFO'}

