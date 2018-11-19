from xcp2k.inputsection import InputSection
from _becke883 import _becke883
from _lyp_adiabatic3 import _lyp_adiabatic3
from _becke88_lr_adiabatic3 import _becke88_lr_adiabatic3
from _becke88_lr3 import _becke88_lr3
from _lyp3 import _lyp3
from _pade3 import _pade3
from _hcth3 import _hcth3
from _optx3 import _optx3
from _libxc3 import _libxc3
from _ke_libxc3 import _ke_libxc3
from _cs13 import _cs13
from _xgga3 import _xgga3
from _ke_gga3 import _ke_gga3
from _p86c3 import _p86c3
from _pw923 import _pw923
from _pz813 import _pz813
from _tfw3 import _tfw3
from _tf3 import _tf3
from _vwn3 import _vwn3
from _xalpha3 import _xalpha3
from _tpss3 import _tpss3
from _pbe3 import _pbe3
from _xwpbe3 import _xwpbe3
from _becke973 import _becke973
from _becke_roussel3 import _becke_roussel3
from _lda_hole_t_c_lr3 import _lda_hole_t_c_lr3
from _pbe_hole_t_c_lr3 import _pbe_hole_t_c_lr3
from _gv093 import _gv093
from _beef3 import _beef3


class _xc_functional3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke883()
        self.LYP_ADIABATIC = _lyp_adiabatic3()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic3()
        self.BECKE88_LR = _becke88_lr3()
        self.LYP = _lyp3()
        self.PADE = _pade3()
        self.HCTH = _hcth3()
        self.OPTX = _optx3()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs13()
        self.XGGA = _xgga3()
        self.KE_GGA = _ke_gga3()
        self.P86C = _p86c3()
        self.PW92 = _pw923()
        self.PZ81 = _pz813()
        self.TFW = _tfw3()
        self.TF = _tf3()
        self.VWN = _vwn3()
        self.XALPHA = _xalpha3()
        self.TPSS = _tpss3()
        self.PBE = _pbe3()
        self.XWPBE = _xwpbe3()
        self.BECKE97 = _becke973()
        self.BECKE_ROUSSEL = _becke_roussel3()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr3()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr3()
        self.GV09 = _gv093()
        self.BEEF = _beef3()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'P86C': 'P86C', 'KE_GGA': 'KE_GGA', 'PW92': 'PW92', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'XALPHA': 'XALPHA', 'LYP': 'LYP', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'OPTX': 'OPTX', 'TF': 'TF', 'CS1': 'CS1', 'BECKE88': 'BECKE88', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'HCTH': 'HCTH', 'PADE': 'PADE', 'PBE': 'PBE', 'GV09': 'GV09', 'BEEF': 'BEEF', 'PZ81': 'PZ81', 'TPSS': 'TPSS', 'XWPBE': 'XWPBE', 'VWN': 'VWN', 'BECKE97': 'BECKE97', 'TFW': 'TFW', 'XGGA': 'XGGA'}
        self._repeated_subsections = {'KE_LIBXC': '_ke_libxc3', 'LIBXC': '_libxc3'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

