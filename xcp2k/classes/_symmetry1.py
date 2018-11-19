from xcp2k.inputsection import InputSection
from _each355 import _each355


class _symmetry1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Molecule = None
        self.Eps_geo = None
        self.Standard_orientation = None
        self.Inertia = None
        self.Symmetry_elements = None
        self.All = None
        self.Rotation_matrices = None
        self.Check_symmetry = None
        self.EACH = _each355()
        self._name = "SYMMETRY"
        self._keywords = {'Rotation_matrices': 'ROTATION_MATRICES', 'All': 'ALL', 'Log_print_key': 'LOG_PRINT_KEY', 'Molecule': 'MOLECULE', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Eps_geo': 'EPS_GEO', 'Symmetry_elements': 'SYMMETRY_ELEMENTS', 'Add_last': 'ADD_LAST', 'Standard_orientation': 'STANDARD_ORIENTATION', 'Check_symmetry': 'CHECK_SYMMETRY', 'Filename': 'FILENAME', 'Inertia': 'INERTIA'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

