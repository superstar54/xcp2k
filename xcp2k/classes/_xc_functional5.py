from xcp2k.inputsection import InputSection
from xcp2k.classes._becke885 import _becke885
from xcp2k.classes._lyp_adiabatic5 import _lyp_adiabatic5
from xcp2k.classes._becke88_lr_adiabatic5 import _becke88_lr_adiabatic5
from xcp2k.classes._becke88_lr5 import _becke88_lr5
from xcp2k.classes._lyp5 import _lyp5
from xcp2k.classes._pade5 import _pade5
from xcp2k.classes._hcth5 import _hcth5
from xcp2k.classes._optx5 import _optx5
from xcp2k.classes._libxc5 import _libxc5
from xcp2k.classes._ke_libxc5 import _ke_libxc5
from xcp2k.classes._cs15 import _cs15
from xcp2k.classes._xgga5 import _xgga5
from xcp2k.classes._ke_gga5 import _ke_gga5
from xcp2k.classes._p86c5 import _p86c5
from xcp2k.classes._pw925 import _pw925
from xcp2k.classes._pz815 import _pz815
from xcp2k.classes._tfw5 import _tfw5
from xcp2k.classes._tf5 import _tf5
from xcp2k.classes._vwn5 import _vwn5
from xcp2k.classes._xalpha5 import _xalpha5
from xcp2k.classes._tpss5 import _tpss5
from xcp2k.classes._pbe5 import _pbe5
from xcp2k.classes._xwpbe5 import _xwpbe5
from xcp2k.classes._becke975 import _becke975
from xcp2k.classes._becke_roussel5 import _becke_roussel5
from xcp2k.classes._lda_hole_t_c_lr5 import _lda_hole_t_c_lr5
from xcp2k.classes._pbe_hole_t_c_lr5 import _pbe_hole_t_c_lr5
from xcp2k.classes._gv095 import _gv095
from xcp2k.classes._beef5 import _beef5
from xcp2k.classes._srlda5 import _srlda5


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
        self.SRLDA = _srlda5()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc5', 'KE_LIBXC': '_ke_libxc5'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

