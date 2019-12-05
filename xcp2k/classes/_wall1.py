from xcp2k.inputsection import InputSection
from xcp2k.classes._reflective1 import _reflective1
from xcp2k.classes._quadratic1 import _quadratic1
from xcp2k.classes._quartic1 import _quartic1
from xcp2k.classes._gaussian1 import _gaussian1


class _wall1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Position = None
        self.REFLECTIVE = _reflective1()
        self.QUADRATIC = _quadratic1()
        self.QUARTIC = _quartic1()
        self.GAUSSIAN = _gaussian1()
        self._name = "WALL"
        self._keywords = {'Type': 'TYPE', 'Position': 'POSITION'}
        self._subsections = {'REFLECTIVE': 'REFLECTIVE', 'QUADRATIC': 'QUADRATIC', 'QUARTIC': 'QUARTIC', 'GAUSSIAN': 'GAUSSIAN'}

