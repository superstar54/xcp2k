from xcp2k.inputsection import InputSection
from xcp2k.classes._print98 import _print98
from xcp2k.classes._ae_basis1 import _ae_basis1
from xcp2k.classes._pp_basis1 import _pp_basis1
from xcp2k.classes._method1 import _method1
from xcp2k.classes._optimization2 import _optimization2
from xcp2k.classes._potential4 import _potential4
from xcp2k.classes._powell1 import _powell1


class _atom1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atomic_number = None
        self.Element = None
        self.Run_type = None
        self.Coulomb_integrals = None
        self.Exchange_integrals = None
        self.Core = None
        self.Electron_configuration = []
        self.Max_angular_momentum = None
        self.Calculate_states = None
        self.Use_gauss_hermite = None
        self.Grid_points_gh = None
        self.PRINT = _print98()
        self.AE_BASIS = _ae_basis1()
        self.PP_BASIS = _pp_basis1()
        self.METHOD_list = []
        self.OPTIMIZATION = _optimization2()
        self.POTENTIAL = _potential4()
        self.POWELL = _powell1()
        self._name = "ATOM"
        self._keywords = {'Atomic_number': 'ATOMIC_NUMBER', 'Element': 'ELEMENT', 'Run_type': 'RUN_TYPE', 'Coulomb_integrals': 'COULOMB_INTEGRALS', 'Exchange_integrals': 'EXCHANGE_INTEGRALS', 'Core': 'CORE', 'Max_angular_momentum': 'MAX_ANGULAR_MOMENTUM', 'Calculate_states': 'CALCULATE_STATES', 'Use_gauss_hermite': 'USE_GAUSS_HERMITE', 'Grid_points_gh': 'GRID_POINTS_GH'}
        self._repeated_keywords = {'Electron_configuration': 'ELECTRON_CONFIGURATION'}
        self._subsections = {'PRINT': 'PRINT', 'AE_BASIS': 'AE_BASIS', 'PP_BASIS': 'PP_BASIS', 'OPTIMIZATION': 'OPTIMIZATION', 'POTENTIAL': 'POTENTIAL', 'POWELL': 'POWELL'}
        self._repeated_subsections = {'METHOD': '_method1'}
        self._attributes = ['METHOD_list']

    def METHOD_add(self, section_parameters=None):
        new_section = _method1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.METHOD_list.append(new_section)
        return new_section

