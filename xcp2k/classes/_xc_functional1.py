from xcp2k.inputsection import InputSection
from xcp2k.classes._becke881 import _becke881
from xcp2k.classes._lyp_adiabatic1 import _lyp_adiabatic1
from xcp2k.classes._becke88_lr_adiabatic1 import _becke88_lr_adiabatic1
from xcp2k.classes._becke88_lr1 import _becke88_lr1
from xcp2k.classes._lyp1 import _lyp1
from xcp2k.classes._pade1 import _pade1
from xcp2k.classes._hcth1 import _hcth1
from xcp2k.classes._optx1 import _optx1
from xcp2k.classes._libxc1 import _libxc1
from xcp2k.classes._ke_libxc1 import _ke_libxc1
from xcp2k.classes._cs11 import _cs11
from xcp2k.classes._xgga1 import _xgga1
from xcp2k.classes._ke_gga1 import _ke_gga1
from xcp2k.classes._p86c1 import _p86c1
from xcp2k.classes._pw921 import _pw921
from xcp2k.classes._pz811 import _pz811
from xcp2k.classes._tfw1 import _tfw1
from xcp2k.classes._tf1 import _tf1
from xcp2k.classes._vwn1 import _vwn1
from xcp2k.classes._xalpha1 import _xalpha1
from xcp2k.classes._tpss1 import _tpss1
from xcp2k.classes._pbe1 import _pbe1
from xcp2k.classes._xwpbe1 import _xwpbe1
from xcp2k.classes._becke971 import _becke971
from xcp2k.classes._becke_roussel1 import _becke_roussel1
from xcp2k.classes._lda_hole_t_c_lr1 import _lda_hole_t_c_lr1
from xcp2k.classes._pbe_hole_t_c_lr1 import _pbe_hole_t_c_lr1
from xcp2k.classes._gv091 import _gv091
from xcp2k.classes._beef1 import _beef1
from xcp2k.classes._srlda1 import _srlda1


class _xc_functional1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke881()
        self.LYP_ADIABATIC = _lyp_adiabatic1()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic1()
        self.BECKE88_LR = _becke88_lr1()
        self.LYP = _lyp1()
        self.PADE = _pade1()
        self.HCTH = _hcth1()
        self.OPTX = _optx1()
        self.LIBXC_list = []
        self.KE_LIBXC_list = []
        self.CS1 = _cs11()
        self.XGGA = _xgga1()
        self.KE_GGA = _ke_gga1()
        self.P86C = _p86c1()
        self.PW92 = _pw921()
        self.PZ81 = _pz811()
        self.TFW = _tfw1()
        self.TF = _tf1()
        self.VWN = _vwn1()
        self.XALPHA = _xalpha1()
        self.TPSS = _tpss1()
        self.PBE = _pbe1()
        self.XWPBE = _xwpbe1()
        self.BECKE97 = _becke971()
        self.BECKE_ROUSSEL = _becke_roussel1()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr1()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr1()
        self.GV09 = _gv091()
        self.BEEF = _beef1()
        self.SRLDA = _srlda1()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc1', 'KE_LIBXC': '_ke_libxc1'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

