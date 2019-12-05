from xcp2k.inputsection import InputSection
from xcp2k.classes._line_search3 import _line_search3


class _cg3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_steep_steps = None
        self.Restart_limit = None
        self.Fletcher_reeves = None
        self.LINE_SEARCH = _line_search3()
        self._name = "CG"
        self._keywords = {'Max_steep_steps': 'MAX_STEEP_STEPS', 'Restart_limit': 'RESTART_LIMIT', 'Fletcher_reeves': 'FLETCHER_REEVES'}
        self._subsections = {'LINE_SEARCH': 'LINE_SEARCH'}

