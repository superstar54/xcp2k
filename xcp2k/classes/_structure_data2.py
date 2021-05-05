from xcp2k.inputsection import InputSection
from xcp2k.classes._each476 import _each476


class _structure_data2(InputSection):
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
        self.EACH = _each476()
        self._name = "STRUCTURE_DATA"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Unit': 'UNIT'}
        self._repeated_keywords = {'Position': 'POSITION', 'Position_scaled': 'POSITION_SCALED', 'Distance': 'DISTANCE', 'Angle': 'ANGLE', 'Dihedral_angle': 'DIHEDRAL_ANGLE'}
        self._subsections = {'EACH': 'EACH'}
        self._repeated_aliases = {'Pos': 'Position', 'Pos_scaled': 'Position_scaled', 'Dis': 'Distance', 'Ang': 'Angle', 'Dihedral': 'Dihedral_angle', 'Dih': 'Dihedral_angle'}
        self._attributes = ['Section_parameters']

