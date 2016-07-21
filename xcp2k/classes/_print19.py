from xcp2k.inputsection import InputSection
from _run_info1 import _run_info1
from _cg_info1 import _cg_info1
from _restart7 import _restart7


class _print19(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RUN_INFO = _run_info1()
        self.CG_INFO = _cg_info1()
        self.RESTART = _restart7()
        self._name = "PRINT"
        self._subsections = {'RUN_INFO': 'RUN_INFO', 'RESTART': 'RESTART', 'CG_INFO': 'CG_INFO'}

