from xcp2k.inputsection import InputSection
from xcp2k.classes._run_info2 import _run_info2


class _print22(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RUN_INFO = _run_info2()
        self._name = "PRINT"
        self._subsections = {'RUN_INFO': 'RUN_INFO'}

