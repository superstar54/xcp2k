from xcp2k.inputsection import InputSection
from _becke884 import _becke884
from _lyp_adiabatic4 import _lyp_adiabatic4
from _becke88_lr_adiabatic4 import _becke88_lr_adiabatic4
from _becke88_lr4 import _becke88_lr4
from _lyp4 import _lyp4
from _pade4 import _pade4
from _hcth4 import _hcth4
from _optx4 import _optx4
from _libxc4 import _libxc4
from _ke_libxc4 import _ke_libxc4
from _cs14 import _cs14
from _xgga4 import _xgga4
from _ke_gga4 import _ke_gga4
from _p86c4 import _p86c4
from _pw924 import _pw924
from _pz814 import _pz814
from _tfw4 import _tfw4
from _tf4 import _tf4
from _vwn4 import _vwn4
from _xalpha4 import _xalpha4
from _tpss4 import _tpss4
from _pbe4 import _pbe4
from _xwpbe4 import _xwpbe4
from _becke974 import _becke974
from _becke_roussel4 import _becke_roussel4
from _lda_hole_t_c_lr4 import _lda_hole_t_c_lr4
from _pbe_hole_t_c_lr4 import _pbe_hole_t_c_lr4
from _gv094 import _gv094
from _beef4 import _beef4


class _xc_functional4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke884()
        self.LYP_ADIABATIC = _lyp_adiabatic4()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic4()
        self.BECKE88_LR = _becke88_lr4()
        self.LYP = _lyp4()
        self.PADE = _pade4()
        self.HCTH = _hcth4()
        self.OPTX = _optx4()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs14()
        self.XGGA = _xgga4()
        self.KE_GGA = _ke_gga4()
        self.P86C = _p86c4()
        self.PW92 = _pw924()
        self.PZ81 = _pz814()
        self.TFW = _tfw4()
        self.TF = _tf4()
        self.VWN = _vwn4()
        self.XALPHA = _xalpha4()
        self.TPSS = _tpss4()
        self.PBE = _pbe4()
        self.XWPBE = _xwpbe4()
        self.BECKE97 = _becke974()
        self.BECKE_ROUSSEL = _becke_roussel4()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr4()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr4()
        self.GV09 = _gv094()
        self.BEEF = _beef4()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'P86C': 'P86C', 'KE_GGA': 'KE_GGA', 'PW92': 'PW92', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'XALPHA': 'XALPHA', 'LYP': 'LYP', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'OPTX': 'OPTX', 'TF': 'TF', 'CS1': 'CS1', 'BECKE88': 'BECKE88', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'HCTH': 'HCTH', 'PADE': 'PADE', 'PBE': 'PBE', 'GV09': 'GV09', 'BEEF': 'BEEF', 'PZ81': 'PZ81', 'TPSS': 'TPSS', 'XWPBE': 'XWPBE', 'VWN': 'VWN', 'BECKE97': 'BECKE97', 'TFW': 'TFW', 'XGGA': 'XGGA'}
        self._repeated_subsections = {'KE_LIBXC': '_ke_libxc4', 'LIBXC': '_libxc4'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

