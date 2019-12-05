from xcp2k.inputsection import InputSection
from xcp2k.classes._weights1 import _weights1
from xcp2k.classes._control1 import _control1


class _flexible_partitioning1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Central_atom = None
        self.Inner_atoms = None
        self.Outer_atoms = None
        self.Inner_radius = None
        self.Outer_radius = None
        self.Strength = None
        self.Bias = None
        self.Temperature = None
        self.Smooth_width = None
        self.WEIGHTS = _weights1()
        self.CONTROL = _control1()
        self._name = "FLEXIBLE_PARTITIONING"
        self._keywords = {'Central_atom': 'CENTRAL_ATOM', 'Inner_atoms': 'INNER_ATOMS', 'Outer_atoms': 'OUTER_ATOMS', 'Inner_radius': 'INNER_RADIUS', 'Outer_radius': 'OUTER_RADIUS', 'Strength': 'STRENGTH', 'Bias': 'BIAS', 'Temperature': 'TEMPERATURE', 'Smooth_width': 'SMOOTH_WIDTH'}
        self._subsections = {'WEIGHTS': 'WEIGHTS', 'CONTROL': 'CONTROL'}

