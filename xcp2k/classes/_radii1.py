from xcp2k.inputsection import InputSection
from xcp2k.classes._each357 import _each357


class _radii1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Core_charges_radii = None
        self.Pgf_radii = None
        self.Set_radii = None
        self.Kind_radii = None
        self.Core_charge_radii = None
        self.Ppl_radii = None
        self.Ppnl_radii = None
        self.Gapw_prj_radii = None
        self.EACH = _each357()
        self._name = "RADII"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Unit': 'UNIT', 'Core_charges_radii': 'CORE_CHARGES_RADII', 'Pgf_radii': 'PGF_RADII', 'Set_radii': 'SET_RADII', 'Kind_radii': 'KIND_RADII', 'Core_charge_radii': 'CORE_CHARGE_RADII', 'Ppl_radii': 'PPL_RADII', 'Ppnl_radii': 'PPNL_RADII', 'Gapw_prj_radii': 'GAPW_PRJ_RADII'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

