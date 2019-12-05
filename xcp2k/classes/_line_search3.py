from xcp2k.inputsection import InputSection
from xcp2k.classes._num2pnt3 import _num2pnt3
from xcp2k.classes._gold3 import _gold3


class _line_search3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self._2PNT = _num2pnt3()
        self.GOLD = _gold3()
        self._name = "LINE_SEARCH"
        self._keywords = {'Type': 'TYPE'}
        self._subsections = {'_2PNT': '2PNT', 'GOLD': 'GOLD'}

