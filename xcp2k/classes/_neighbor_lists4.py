from xcp2k.inputsection import InputSection
from xcp2k.classes._each339 import _each339


class _neighbor_lists4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Sab_orb = None
        self.Sab_aux_fit = None
        self.Sab_aux_fit_vs_orb = None
        self.Sab_scp = None
        self.Sab_vdw = None
        self.Sab_cn = None
        self.Sac_ae = None
        self.Sac_ppl = None
        self.Sap_ppnl = None
        self.Sap_oce = None
        self.Sab_se = None
        self.Sab_lrc = None
        self.Sab_tbe = None
        self.Sab_core = None
        self.Sab_xb = None
        self.Sab_xtb_nonbond = None
        self.Soo_list = None
        self.Sip_list = None
        self.EACH = _each339()
        self._name = "NEIGHBOR_LISTS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Unit': 'UNIT', 'Sab_orb': 'SAB_ORB', 'Sab_aux_fit': 'SAB_AUX_FIT', 'Sab_aux_fit_vs_orb': 'SAB_AUX_FIT_VS_ORB', 'Sab_scp': 'SAB_SCP', 'Sab_vdw': 'SAB_VDW', 'Sab_cn': 'SAB_CN', 'Sac_ae': 'SAC_AE', 'Sac_ppl': 'SAC_PPL', 'Sap_ppnl': 'SAP_PPNL', 'Sap_oce': 'SAP_OCE', 'Sab_se': 'SAB_SE', 'Sab_lrc': 'SAB_LRC', 'Sab_tbe': 'SAB_TBE', 'Sab_core': 'SAB_CORE', 'Sab_xb': 'SAB_XB', 'Sab_xtb_nonbond': 'SAB_XTB_NONBOND', 'Soo_list': 'SOO_LIST', 'Sip_list': 'SIP_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

