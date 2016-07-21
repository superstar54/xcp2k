from xcp2k.inputsection import InputSection
from _each299 import _each299


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
        self.Gth_ppl_radii = None
        self.Gth_ppnl_radii = None
        self.Gapw_prj_radii = None
        self.EACH = _each299()
        self._name = "RADII"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Pgf_radii': 'PGF_RADII', 'Core_charges_radii': 'CORE_CHARGES_RADII', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Gapw_prj_radii': 'GAPW_PRJ_RADII', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Core_charge_radii': 'CORE_CHARGE_RADII', 'Kind_radii': 'KIND_RADII', 'Set_radii': 'SET_RADII', 'Gth_ppnl_radii': 'GTH_PPNL_RADII', 'Gth_ppl_radii': 'GTH_PPL_RADII', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

