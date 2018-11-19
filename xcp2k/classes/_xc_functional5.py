from xcp2k.inputsection import InputSection
from _becke885 import _becke885
from _lyp_adiabatic5 import _lyp_adiabatic5
from _becke88_lr_adiabatic5 import _becke88_lr_adiabatic5
from _becke88_lr5 import _becke88_lr5
from _lyp5 import _lyp5
from _pade5 import _pade5
from _hcth5 import _hcth5
from _optx5 import _optx5
from _libxc5 import _libxc5
from _ke_libxc5 import _ke_libxc5
from _cs15 import _cs15
from _xgga5 import _xgga5
from _ke_gga5 import _ke_gga5
from _p86c5 import _p86c5
from _pw925 import _pw925
from _pz815 import _pz815
from _tfw5 import _tfw5
from _tf5 import _tf5
from _vwn5 import _vwn5
from _xalpha5 import _xalpha5
from _tpss5 import _tpss5
from _pbe5 import _pbe5
from _xwpbe5 import _xwpbe5
from _becke975 import _becke975
from _becke_roussel5 import _becke_roussel5
from _lda_hole_t_c_lr5 import _lda_hole_t_c_lr5
from _pbe_hole_t_c_lr5 import _pbe_hole_t_c_lr5
from _gv095 import _gv095
from _beef5 import _beef5


class _xc_functional5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke885()
        self.LYP_ADIABATIC = _lyp_adiabatic5()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic5()
        self.BECKE88_LR = _becke88_lr5()
        self.LYP = _lyp5()
        self.PADE = _pade5()
        self.HCTH = _hcth5()
        self.OPTX = _optx5()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs15()
        self.XGGA = _xgga5()
        self.KE_GGA = _ke_gga5()
        self.P86C = _p86c5()
        self.PW92 = _pw925()
        self.PZ81 = _pz815()
        self.TFW = _tfw5()
        self.TF = _tf5()
        self.VWN = _vwn5()
        self.XALPHA = _xalpha5()
        self.TPSS = _tpss5()
        self.PBE = _pbe5()
        self.XWPBE = _xwpbe5()
        self.BECKE97 = _becke975()
        self.BECKE_ROUSSEL = _becke_roussel5()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr5()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr5()
        self.GV09 = _gv095()
        self.BEEF = _beef5()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'P86C': 'P86C', 'KE_GGA': 'KE_GGA', 'PW92': 'PW92', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'XALPHA': 'XALPHA', 'LYP': 'LYP', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'OPTX': 'OPTX', 'TF': 'TF', 'CS1': 'CS1', 'BECKE88': 'BECKE88', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'HCTH': 'HCTH', 'PADE': 'PADE', 'PBE': 'PBE', 'GV09': 'GV09', 'BEEF': 'BEEF', 'PZ81': 'PZ81', 'TPSS': 'TPSS', 'XWPBE': 'XWPBE', 'VWN': 'VWN', 'BECKE97': 'BECKE97', 'TFW': 'TFW', 'XGGA': 'XGGA'}
        self._repeated_subsections = {'KE_LIBXC': '_ke_libxc5', 'LIBXC': '_libxc5'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

