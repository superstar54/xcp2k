from xcp2k.inputsection import InputSection
from _line_search1 import _line_search1


class _cg1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_steep_steps = None
        self.Restart_limit = None
        self.Fletcher_reeves = None
        self.LINE_SEARCH = _line_search1()
        self._name = "CG"
        self._keywords = {'Restart_limit': 'RESTART_LIMIT', 'Max_steep_steps': 'MAX_STEEP_STEPS', 'Fletcher_reeves': 'FLETCHER_REEVES'}
        self._subsections = {'LINE_SEARCH': 'LINE_SEARCH'}

