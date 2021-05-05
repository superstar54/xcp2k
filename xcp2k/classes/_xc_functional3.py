from xcp2k.inputsection import InputSection
from xcp2k.classes._becke883 import _becke883
from xcp2k.classes._lyp_adiabatic3 import _lyp_adiabatic3
from xcp2k.classes._becke88_lr_adiabatic3 import _becke88_lr_adiabatic3
from xcp2k.classes._becke88_lr3 import _becke88_lr3
from xcp2k.classes._lyp3 import _lyp3
from xcp2k.classes._pade3 import _pade3
from xcp2k.classes._hcth3 import _hcth3
from xcp2k.classes._optx3 import _optx3
from xcp2k.classes._libxc3 import _libxc3
from xcp2k.classes._ke_libxc3 import _ke_libxc3
from xcp2k.classes._cs13 import _cs13
from xcp2k.classes._xgga3 import _xgga3
from xcp2k.classes._ke_gga3 import _ke_gga3
from xcp2k.classes._p86c3 import _p86c3
from xcp2k.classes._pw923 import _pw923
from xcp2k.classes._pz813 import _pz813
from xcp2k.classes._tfw3 import _tfw3
from xcp2k.classes._tf3 import _tf3
from xcp2k.classes._vwn3 import _vwn3
from xcp2k.classes._xalpha3 import _xalpha3
from xcp2k.classes._tpss3 import _tpss3
from xcp2k.classes._pbe3 import _pbe3
from xcp2k.classes._xwpbe3 import _xwpbe3
from xcp2k.classes._becke973 import _becke973
from xcp2k.classes._becke_roussel3 import _becke_roussel3
from xcp2k.classes._lda_hole_t_c_lr3 import _lda_hole_t_c_lr3
from xcp2k.classes._pbe_hole_t_c_lr3 import _pbe_hole_t_c_lr3
from xcp2k.classes._gv093 import _gv093
from xcp2k.classes._beef3 import _beef3
from xcp2k.classes._srlda3 import _srlda3


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
        self.SRLDA = _srlda3()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc3', 'KE_LIBXC': '_ke_libxc3'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

