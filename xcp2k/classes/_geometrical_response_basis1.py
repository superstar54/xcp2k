from xcp2k.inputsection import InputSection
from xcp2k.classes._each636 import _each636


class _geometrical_response_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Delta_charge = None
        self.Derivatives = None
        self.Quadrature = None
        self.Grid_points = None
        self.Num_gto_core = None
        self.Num_gto_extended = None
        self.Num_gto_polarization = None
        self.Extension_basis = None
        self.Geometrical_factor = None
        self.Geo_start_value = None
        self.Confinement = None
        self.Name_body = None
        self.EACH = _each636()
        self._name = "GEOMETRICAL_RESPONSE_BASIS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Delta_charge': 'DELTA_CHARGE', 'Derivatives': 'DERIVATIVES', 'Quadrature': 'QUADRATURE', 'Grid_points': 'GRID_POINTS', 'Num_gto_core': 'NUM_GTO_CORE', 'Num_gto_extended': 'NUM_GTO_EXTENDED', 'Num_gto_polarization': 'NUM_GTO_POLARIZATION', 'Extension_basis': 'EXTENSION_BASIS', 'Geometrical_factor': 'GEOMETRICAL_FACTOR', 'Geo_start_value': 'GEO_START_VALUE', 'Confinement': 'CONFINEMENT', 'Name_body': 'NAME_BODY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

