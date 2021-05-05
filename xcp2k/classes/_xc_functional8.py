from xcp2k.inputsection import InputSection
from xcp2k.classes._becke888 import _becke888
from xcp2k.classes._lyp_adiabatic8 import _lyp_adiabatic8
from xcp2k.classes._becke88_lr_adiabatic8 import _becke88_lr_adiabatic8
from xcp2k.classes._becke88_lr8 import _becke88_lr8
from xcp2k.classes._lyp8 import _lyp8
from xcp2k.classes._pade8 import _pade8
from xcp2k.classes._hcth8 import _hcth8
from xcp2k.classes._optx8 import _optx8
from xcp2k.classes._libxc8 import _libxc8
from xcp2k.classes._ke_libxc8 import _ke_libxc8
from xcp2k.classes._cs18 import _cs18
from xcp2k.classes._xgga8 import _xgga8
from xcp2k.classes._ke_gga8 import _ke_gga8
from xcp2k.classes._p86c8 import _p86c8
from xcp2k.classes._pw928 import _pw928
from xcp2k.classes._pz818 import _pz818
from xcp2k.classes._tfw8 import _tfw8
from xcp2k.classes._tf8 import _tf8
from xcp2k.classes._vwn8 import _vwn8
from xcp2k.classes._xalpha8 import _xalpha8
from xcp2k.classes._tpss8 import _tpss8
from xcp2k.classes._pbe8 import _pbe8
from xcp2k.classes._xwpbe8 import _xwpbe8
from xcp2k.classes._becke978 import _becke978
from xcp2k.classes._becke_roussel8 import _becke_roussel8
from xcp2k.classes._lda_hole_t_c_lr8 import _lda_hole_t_c_lr8
from xcp2k.classes._pbe_hole_t_c_lr8 import _pbe_hole_t_c_lr8
from xcp2k.classes._gv098 import _gv098
from xcp2k.classes._beef8 import _beef8
from xcp2k.classes._srlda8 import _srlda8


class _xc_functional8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke888()
        self.LYP_ADIABATIC = _lyp_adiabatic8()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic8()
        self.BECKE88_LR = _becke88_lr8()
        self.LYP = _lyp8()
        self.PADE = _pade8()
        self.HCTH = _hcth8()
        self.OPTX = _optx8()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs18()
        self.XGGA = _xgga8()
        self.KE_GGA = _ke_gga8()
        self.P86C = _p86c8()
        self.PW92 = _pw928()
        self.PZ81 = _pz818()
        self.TFW = _tfw8()
        self.TF = _tf8()
        self.VWN = _vwn8()
        self.XALPHA = _xalpha8()
        self.TPSS = _tpss8()
        self.PBE = _pbe8()
        self.XWPBE = _xwpbe8()
        self.BECKE97 = _becke978()
        self.BECKE_ROUSSEL = _becke_roussel8()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr8()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr8()
        self.GV09 = _gv098()
        self.BEEF = _beef8()
        self.SRLDA = _srlda8()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc8', 'KE_LIBXC': '_ke_libxc8'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

