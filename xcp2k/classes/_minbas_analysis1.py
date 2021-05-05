from xcp2k.inputsection import InputSection
from xcp2k.classes._each386 import _each386
from xcp2k.classes._minbas_cube1 import _minbas_cube1
from xcp2k.classes._minbas_molden1 import _minbas_molden1


class _minbas_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Eps_filter = None
        self.Full_orthogonalization = None
        self.Bond_order = None
        self.EACH = _each386()
        self.MINBAS_CUBE = _minbas_cube1()
        self.MINBAS_MOLDEN = _minbas_molden1()
        self._name = "MINBAS_ANALYSIS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Eps_filter': 'EPS_FILTER', 'Full_orthogonalization': 'FULL_ORTHOGONALIZATION', 'Bond_order': 'BOND_ORDER'}
        self._subsections = {'EACH': 'EACH', 'MINBAS_CUBE': 'MINBAS_CUBE', 'MINBAS_MOLDEN': 'MINBAS_MOLDEN'}
        self._attributes = ['Section_parameters']

