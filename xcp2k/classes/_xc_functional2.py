from xcp2k.inputsection import InputSection
from _becke882 import _becke882
from _lyp_adiabatic2 import _lyp_adiabatic2
from _becke88_lr_adiabatic2 import _becke88_lr_adiabatic2
from _becke88_lr2 import _becke88_lr2
from _lyp2 import _lyp2
from _pade2 import _pade2
from _hcth2 import _hcth2
from _optx2 import _optx2
from _libxc2 import _libxc2
from _ke_libxc2 import _ke_libxc2
from _cs12 import _cs12
from _xgga2 import _xgga2
from _ke_gga2 import _ke_gga2
from _p86c2 import _p86c2
from _pw922 import _pw922
from _pz812 import _pz812
from _tfw2 import _tfw2
from _tf2 import _tf2
from _vwn2 import _vwn2
from _xalpha2 import _xalpha2
from _tpss2 import _tpss2
from _pbe2 import _pbe2
from _xwpbe2 import _xwpbe2
from _becke972 import _becke972
from _becke_roussel2 import _becke_roussel2
from _lda_hole_t_c_lr2 import _lda_hole_t_c_lr2
from _pbe_hole_t_c_lr2 import _pbe_hole_t_c_lr2
from _gv092 import _gv092
from _beef2 import _beef2


class _xc_functional2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke882()
        self.LYP_ADIABATIC = _lyp_adiabatic2()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic2()
        self.BECKE88_LR = _becke88_lr2()
        self.LYP = _lyp2()
        self.PADE = _pade2()
        self.HCTH = _hcth2()
        self.OPTX = _optx2()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs12()
        self.XGGA = _xgga2()
        self.KE_GGA = _ke_gga2()
        self.P86C = _p86c2()
        self.PW92 = _pw922()
        self.PZ81 = _pz812()
        self.TFW = _tfw2()
        self.TF = _tf2()
        self.VWN = _vwn2()
        self.XALPHA = _xalpha2()
        self.TPSS = _tpss2()
        self.PBE = _pbe2()
        self.XWPBE = _xwpbe2()
        self.BECKE97 = _becke972()
        self.BECKE_ROUSSEL = _becke_roussel2()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr2()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr2()
        self.GV09 = _gv092()
        self.BEEF = _beef2()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'P86C': 'P86C', 'KE_GGA': 'KE_GGA', 'PW92': 'PW92', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'XALPHA': 'XALPHA', 'LYP': 'LYP', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'OPTX': 'OPTX', 'TF': 'TF', 'CS1': 'CS1', 'BECKE88': 'BECKE88', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'HCTH': 'HCTH', 'PADE': 'PADE', 'PBE': 'PBE', 'GV09': 'GV09', 'BEEF': 'BEEF', 'PZ81': 'PZ81', 'TPSS': 'TPSS', 'XWPBE': 'XWPBE', 'VWN': 'VWN', 'BECKE97': 'BECKE97', 'TFW': 'TFW', 'XGGA': 'XGGA'}
        self._repeated_subsections = {'KE_LIBXC': '_ke_libxc2', 'LIBXC': '_libxc2'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

