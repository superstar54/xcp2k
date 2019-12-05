from xcp2k.inputsection import InputSection
from xcp2k.classes._bonds1 import _bonds1
from xcp2k.classes._angles1 import _angles1
from xcp2k.classes._torsions1 import _torsions1
from xcp2k.classes._impropers1 import _impropers1


class _merge_molecules1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.BONDS = _bonds1()
        self.ANGLES = _angles1()
        self.TORSIONS = _torsions1()
        self.IMPROPERS = _impropers1()
        self._name = "MERGE_MOLECULES"
        self._subsections = {'BONDS': 'BONDS', 'ANGLES': 'ANGLES', 'TORSIONS': 'TORSIONS', 'IMPROPERS': 'IMPROPERS'}

