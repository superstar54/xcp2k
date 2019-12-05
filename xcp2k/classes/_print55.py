from xcp2k.inputsection import InputSection
from xcp2k.classes._atomic_coordinates1 import _atomic_coordinates1
from xcp2k.classes._structure_data2 import _structure_data2
from xcp2k.classes._interatomic_distances1 import _interatomic_distances1
from xcp2k.classes._topology_info1 import _topology_info1
from xcp2k.classes._cell5 import _cell5
from xcp2k.classes._kinds1 import _kinds1
from xcp2k.classes._symmetry1 import _symmetry1
from xcp2k.classes._molecules1 import _molecules1
from xcp2k.classes._radii1 import _radii1


class _print55(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ATOMIC_COORDINATES = _atomic_coordinates1()
        self.STRUCTURE_DATA = _structure_data2()
        self.INTERATOMIC_DISTANCES = _interatomic_distances1()
        self.TOPOLOGY_INFO = _topology_info1()
        self.CELL = _cell5()
        self.KINDS = _kinds1()
        self.SYMMETRY = _symmetry1()
        self.MOLECULES = _molecules1()
        self.RADII = _radii1()
        self._name = "PRINT"
        self._subsections = {'ATOMIC_COORDINATES': 'ATOMIC_COORDINATES', 'STRUCTURE_DATA': 'STRUCTURE_DATA', 'INTERATOMIC_DISTANCES': 'INTERATOMIC_DISTANCES', 'TOPOLOGY_INFO': 'TOPOLOGY_INFO', 'CELL': 'CELL', 'KINDS': 'KINDS', 'SYMMETRY': 'SYMMETRY', 'MOLECULES': 'MOLECULES', 'RADII': 'RADII'}

