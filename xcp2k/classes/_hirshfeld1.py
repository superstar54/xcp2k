from xcp2k.inputsection import InputSection
from _each268 import _each268


class _hirshfeld1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Self_consistent = None
        self.Shape_function = None
        self.Reference_charge = None
        self.User_radius = None
        self.Atomic_radii = None
        self.EACH = _each268()
        self._name = "HIRSHFELD"
        self._keywords = {'Reference_charge': 'REFERENCE_CHARGE', 'Log_print_key': 'LOG_PRINT_KEY', 'User_radius': 'USER_RADIUS', 'Shape_function': 'SHAPE_FUNCTION', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Atomic_radii': 'ATOMIC_RADII', 'Add_last': 'ADD_LAST', 'Self_consistent': 'SELF_CONSISTENT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

