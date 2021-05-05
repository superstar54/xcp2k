from xcp2k.inputsection import InputSection
from xcp2k.classes._each401 import _each401
from xcp2k.classes._density_gradient1 import _density_gradient1
from xcp2k.classes._dielectric_function1 import _dielectric_function1
from xcp2k.classes._total_charge_density1 import _total_charge_density1
from xcp2k.classes._polarisation_charge_density1 import _polarisation_charge_density1
from xcp2k.classes._polarisation_potential1 import _polarisation_potential1


class _sccs1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each401()
        self.DENSITY_GRADIENT = _density_gradient1()
        self.DIELECTRIC_FUNCTION = _dielectric_function1()
        self.TOTAL_CHARGE_DENSITY = _total_charge_density1()
        self.POLARISATION_CHARGE_DENSITY = _polarisation_charge_density1()
        self.POLARISATION_POTENTIAL = _polarisation_potential1()
        self._name = "SCCS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._subsections = {'EACH': 'EACH', 'DENSITY_GRADIENT': 'DENSITY_GRADIENT', 'DIELECTRIC_FUNCTION': 'DIELECTRIC_FUNCTION', 'TOTAL_CHARGE_DENSITY': 'TOTAL_CHARGE_DENSITY', 'POLARISATION_CHARGE_DENSITY': 'POLARISATION_CHARGE_DENSITY', 'POLARISATION_POTENTIAL': 'POLARISATION_POTENTIAL'}
        self._attributes = ['Section_parameters']

