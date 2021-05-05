from xcp2k.inputsection import InputSection
from xcp2k.classes._becke884 import _becke884
from xcp2k.classes._lyp_adiabatic4 import _lyp_adiabatic4
from xcp2k.classes._becke88_lr_adiabatic4 import _becke88_lr_adiabatic4
from xcp2k.classes._becke88_lr4 import _becke88_lr4
from xcp2k.classes._lyp4 import _lyp4
from xcp2k.classes._pade4 import _pade4
from xcp2k.classes._hcth4 import _hcth4
from xcp2k.classes._optx4 import _optx4
from xcp2k.classes._libxc4 import _libxc4
from xcp2k.classes._ke_libxc4 import _ke_libxc4
from xcp2k.classes._cs14 import _cs14
from xcp2k.classes._xgga4 import _xgga4
from xcp2k.classes._ke_gga4 import _ke_gga4
from xcp2k.classes._p86c4 import _p86c4
from xcp2k.classes._pw924 import _pw924
from xcp2k.classes._pz814 import _pz814
from xcp2k.classes._tfw4 import _tfw4
from xcp2k.classes._tf4 import _tf4
from xcp2k.classes._vwn4 import _vwn4
from xcp2k.classes._xalpha4 import _xalpha4
from xcp2k.classes._tpss4 import _tpss4
from xcp2k.classes._pbe4 import _pbe4
from xcp2k.classes._xwpbe4 import _xwpbe4
from xcp2k.classes._becke974 import _becke974
from xcp2k.classes._becke_roussel4 import _becke_roussel4
from xcp2k.classes._lda_hole_t_c_lr4 import _lda_hole_t_c_lr4
from xcp2k.classes._pbe_hole_t_c_lr4 import _pbe_hole_t_c_lr4
from xcp2k.classes._gv094 import _gv094
from xcp2k.classes._beef4 import _beef4
from xcp2k.classes._srlda4 import _srlda4


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
        self.SRLDA = _srlda4()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88': 'BECKE88', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'PADE': 'PADE', 'HCTH': 'HCTH', 'OPTX': 'OPTX', 'CS1': 'CS1', 'XGGA': 'XGGA', 'KE_GGA': 'KE_GGA', 'P86C': 'P86C', 'PW92': 'PW92', 'PZ81': 'PZ81', 'TFW': 'TFW', 'TF': 'TF', 'VWN': 'VWN', 'XALPHA': 'XALPHA', 'TPSS': 'TPSS', 'PBE': 'PBE', 'XWPBE': 'XWPBE', 'BECKE97': 'BECKE97', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'GV09': 'GV09', 'BEEF': 'BEEF', 'SRLDA': 'SRLDA'}
        self._repeated_subsections = {'LIBXC': '_libxc4', 'KE_LIBXC': '_ke_libxc4'}
        self._attributes = ['Section_parameters', 'LIBXC_list', 'KE_LIBXC_list']

    def LIBXC_add(self, section_parameters=None):
        new_section = _libxc4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LIBXC_list.append(new_section)
        return new_section

    def KE_LIBXC_add(self, section_parameters=None):
        new_section = _ke_libxc4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_LIBXC_list.append(new_section)
        return new_section

