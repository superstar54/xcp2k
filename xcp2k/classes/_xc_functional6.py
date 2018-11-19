from xcp2k.inputsection import InputSection
from _becke886 import _becke886
from _lyp_adiabatic6 import _lyp_adiabatic6
from _becke88_lr_adiabatic6 import _becke88_lr_adiabatic6
from _becke88_lr6 import _becke88_lr6
from _lyp6 import _lyp6
from _pade6 import _pade6
from _hcth6 import _hcth6
from _optx6 import _optx6
from _libxc6 import _libxc6
from _ke_libxc6 import _ke_libxc6
from _cs16 import _cs16
from _xgga6 import _xgga6
from _ke_gga6 import _ke_gga6
from _p86c6 import _p86c6
from _pw926 import _pw926
from _pz816 import _pz816
from _tfw6 import _tfw6
from _tf6 import _tf6
from _vwn6 import _vwn6
from _xalpha6 import _xalpha6
from _tpss6 import _tpss6
from _pbe6 import _pbe6
from _xwpbe6 import _xwpbe6
from _becke976 import _becke976
from _becke_roussel6 import _becke_roussel6
from _lda_hole_t_c_lr6 import _lda_hole_t_c_lr6
from _pbe_hole_t_c_lr6 import _pbe_hole_t_c_lr6
from _gv096 import _gv096
from _beef6 import _beef6


class _xc_functional6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke886()
        self.LYP_ADIABATIC = _lyp_adiabatic6()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic6()
        self.BECKE88_LR = _becke88_lr6()
        self.LYP = _lyp6()
        self.PADE = _pade6()
        self.HCTH = _hcth6()
        self.OPTX = _optx6()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs16()
        self.XGGA = _xgga6()
        self.KE_GGA = _ke_gga6()
        self.P86C = _p86c6()
        self.PW92 = _pw926()
        self.PZ81 = _pz816()
        self.TFW = _tfw6()
        self.TF = _tf6()
        self.VWN = _vwn6()
        self.XALPHA = _xalpha6()
        self.TPSS = _tpss6()
        self.PBE = _pbe6()
        self.XWPBE = _xwpbe6()
        self.BECKE97 = _becke976()
        self.BECKE_ROUSSEL = _becke_roussel6()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr6()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr6()
        self.GV09 = _gv096()
        self.BEEF = _beef6()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'P86C': 'P86C', 'KE_GGA': 'KE_GGA', 'PW92': 'PW92', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'XALPHA': 'XALPHA', 'LYP': 'LYP', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'OPTX': 'OPTX', 'TF': 'TF', 'CS1': 'CS1', 'BECKE88': 'BECKE88', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'HCTH': 'HCTH', 'PADE': 'PADE', 'PBE': 'PBE', 'GV09': 'GV09', 'BEEF': 'BEEF', 'PZ81': 'PZ81', 'TPSS': 'TPSS', 'XWPBE': 'XWPBE', 'VWN': 'VWN', 'BECKE97': 'BECKE97', 'TFW': 'TFW', 'XGGA': 'XGGA'}
        self._repeated_subsections = {'KE_LIBXC': '_ke_libxc6', 'LIBXC': '_libxc6'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc6()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc6()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

