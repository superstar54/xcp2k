from xcp2k.inputsection import InputSection
from _each284 import _each284
from _density_gradient1 import _density_gradient1
from _dielectric_function1 import _dielectric_function1
from _polarisation_potential1 import _polarisation_potential1


class _sccs1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each284()
        self.DENSITY_GRADIENT = _density_gradient1()
        self.DIELECTRIC_FUNCTION = _dielectric_function1()
        self.POLARISATION_POTENTIAL = _polarisation_potential1()
        self._name = "SCCS"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'POLARISATION_POTENTIAL': 'POLARISATION_POTENTIAL', 'DENSITY_GRADIENT': 'DENSITY_GRADIENT', 'DIELECTRIC_FUNCTION': 'DIELECTRIC_FUNCTION', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

