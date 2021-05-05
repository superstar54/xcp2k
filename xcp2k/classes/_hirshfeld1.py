from xcp2k.inputsection import InputSection
from xcp2k.classes._each384 import _each384


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
        self.EACH = _each384()
        self._name = "HIRSHFELD"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Self_consistent': 'SELF_CONSISTENT', 'Shape_function': 'SHAPE_FUNCTION', 'Reference_charge': 'REFERENCE_CHARGE', 'User_radius': 'USER_RADIUS', 'Atomic_radii': 'ATOMIC_RADII'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

