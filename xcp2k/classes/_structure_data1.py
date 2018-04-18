from xcp2k.inputsection import InputSection
from _each88 import _each88


class _structure_data1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Position = []
        self.Pos = self.Position
        self.Position_scaled = []
        self.Pos_scaled = self.Position_scaled
        self.Distance = []
        self.Dis = self.Distance
        self.Angle = []
        self.Ang = self.Angle
        self.Dihedral_angle = []
        self.Dihedral = self.Dihedral_angle
        self.Dih = self.Dihedral_angle
        self.EACH = _each88()
        self._name = "STRUCTURE_DATA"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Unit': 'UNIT', 'Filename': 'FILENAME'}
        self._repeated_keywords = {'Position': 'POSITION', 'Dihedral_angle': 'DIHEDRAL_ANGLE', 'Angle': 'ANGLE', 'Position_scaled': 'POSITION_SCALED', 'Distance': 'DISTANCE'}
        self._subsections = {'EACH': 'EACH'}
        self._repeated_aliases = {'Ang': 'Angle', 'Dih': 'Dihedral_angle', 'Dihedral': 'Dihedral_angle', 'Pos': 'Position', 'Pos_scaled': 'Position_scaled', 'Dis': 'Distance'}
        self._attributes = ['Section_parameters']

