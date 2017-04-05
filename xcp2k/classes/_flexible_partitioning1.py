from xcp2k.inputsection import InputSection
from _weights1 import _weights1
from _control1 import _control1


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
        self._keywords = {'Strength': 'STRENGTH', 'Inner_radius': 'INNER_RADIUS', 'Inner_atoms': 'INNER_ATOMS', 'Central_atom': 'CENTRAL_ATOM', 'Smooth_width': 'SMOOTH_WIDTH', 'Outer_atoms': 'OUTER_ATOMS', 'Outer_radius': 'OUTER_RADIUS', 'Bias': 'BIAS', 'Temperature': 'TEMPERATURE'}
        self._subsections = {'CONTROL': 'CONTROL', 'WEIGHTS': 'WEIGHTS'}

