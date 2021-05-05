from xcp2k.inputsection import InputSection
from xcp2k.classes._becke882 import _becke882
from xcp2k.classes._lyp_adiabatic2 import _lyp_adiabatic2
from xcp2k.classes._becke88_lr_adiabatic2 import _becke88_lr_adiabatic2
from xcp2k.classes._becke88_lr2 import _becke88_lr2
from xcp2k.classes._lyp2 import _lyp2
from xcp2k.classes._pade2 import _pade2
from xcp2k.classes._hcth2 import _hcth2
from xcp2k.classes._optx2 import _optx2
from xcp2k.classes._libxc2 import _libxc2
from xcp2k.classes._ke_libxc2 import _ke_libxc2
from xcp2k.classes._cs12 import _cs12
from xcp2k.classes._xgga2 import _xgga2
from xcp2k.classes._ke_gga2 import _ke_gga2
from xcp2k.classes._p86c2 import _p86c2
from xcp2k.classes._pw922 import _pw922
from xcp2k.classes._pz812 import _pz812
from xcp2k.classes._tfw2 import _tfw2
from xcp2k.classes._tf2 import _tf2
from xcp2k.classes._vwn2 import _vwn2
from xcp2k.classes._xalpha2 import _xalpha2
from xcp2k.classes._tpss2 import _tpss2
from xcp2k.classes._pbe2 import _pbe2
from xcp2k.classes._xwpbe2 import _xwpbe2
from xcp2k.classes._becke972 import _becke972
from xcp2k.classes._becke_roussel2 import _becke_roussel2
from xcp2k.classes._lda_hole_t_c_lr2 import _lda_hole_t_c_lr2
from xcp2k.classes._pbe_hole_t_c_lr2 import _pbe_hole_t_c_lr2
from xcp2k.classes._gv092 import _gv092
from xcp2k.classes._beef2 import _beef2
from xcp2k.classes._srlda2 import _srlda2


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
        self.SRLDA = _srlda2()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc2', 'KE_LIBXC': '_ke_libxc2'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

