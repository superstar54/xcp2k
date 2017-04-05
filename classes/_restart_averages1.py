from xcp2k.inputsection import InputSection


class _restart_averages1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Itimes_start = None
        self.Avecpu = None
        self.Avehugoniot = None
        self.Avetemp_baro = None
        self.Avepot = None
        self.Avekin = None
        self.Avetemp = None
        self.Avekin_qm = None
        self.Avetemp_qm = None
        self.Avevol = None
        self.Avecell_a = None
        self.Avecell_b = None
        self.Avecell_c = None
        self.Avealpha = None
        self.Avebeta = None
        self.Avegamma = None
        self.Ave_econs = None
        self.Ave_press = None
        self.Ave_pxx = None
        self.Ave_pv_vir = None
        self.Ave_pv_tot = None
        self.Ave_pv_kin = None
        self.Ave_pv_cnstr = None
        self.Ave_pv_xc = None
        self.Ave_pv_fock_4c = None
        self.Ave_colvars = None
        self.Ave_mmatrix = None
        self._name = "RESTART_AVERAGES"
        self._keywords = {'Ave_econs': 'AVE_ECONS', 'Avehugoniot': 'AVEHUGONIOT', 'Ave_pv_xc': 'AVE_PV_XC', 'Ave_pv_vir': 'AVE_PV_VIR', 'Ave_pv_tot': 'AVE_PV_TOT', 'Avekin': 'AVEKIN', 'Avepot': 'AVEPOT', 'Ave_pv_kin': 'AVE_PV_KIN', 'Avealpha': 'AVEALPHA', 'Avebeta': 'AVEBETA', 'Itimes_start': 'ITIMES_START', 'Avegamma': 'AVEGAMMA', 'Ave_pxx': 'AVE_PXX', 'Ave_pv_fock_4c': 'AVE_PV_FOCK_4C', 'Avetemp_qm': 'AVETEMP_QM', 'Avecell_b': 'AVECELL_B', 'Avecell_c': 'AVECELL_C', 'Ave_pv_cnstr': 'AVE_PV_CNSTR', 'Avecell_a': 'AVECELL_A', 'Avekin_qm': 'AVEKIN_QM', 'Avetemp_baro': 'AVETEMP_BARO', 'Avevol': 'AVEVOL', 'Ave_colvars': 'AVE_COLVARS', 'Ave_mmatrix': 'AVE_MMATRIX', 'Avetemp': 'AVETEMP', 'Avecpu': 'AVECPU', 'Ave_press': 'AVE_PRESS'}

