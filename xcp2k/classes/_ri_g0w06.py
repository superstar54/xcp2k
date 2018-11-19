from xcp2k.inputsection import InputSection
from _periodic19 import _periodic19
from _bse6 import _bse6
from _ic6 import _ic6


class _ri_g0w06(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Corr_mos_occ = None
        self.Corr_mos_virt = None
        self.Scaling = None
        self.Numb_poles = None
        self.Omega_max_fit = None
        self.Stop_crit = None
        self.Print_fit_error = None
        self.Max_iter_fit = None
        self.Check_fit = None
        self.Crossing_search = None
        self.Fermi_level_offset = None
        self.Ev_sc_iter = None
        self.Eps_ev_sc_iter = None
        self.Hf_like_ev_start = None
        self.Ev_sc_gw_remove_neg_virt_energies = None
        self.Print_gw_details = None
        self.Ri_sigma_x = None
        self.Normalize_sigma = None
        self.Neglect_normalization_sigma_x = None
        self.Ri_metric = None
        self.Mix_exchange = None
        self.Fraction_exx = None
        self.Contour_def_start = None
        self.Contour_def_end = None
        self.Contour_def_offset = None
        self.Atoms = None
        self.Atom_range = None
        self.Eps_charge = None
        self.Ic_corr_list = None
        self.Ic_corr_list_beta = None
        self.Periodic = None
        self.Bse = None
        self.Image_charge_model = None
        self.Analytic_continuation = None
        self.Nparam_pade = None
        self.PERIODIC = _periodic19()
        self.BSE = _bse6()
        self.IC = _ic6()
        self._name = "RI_G0W0"
        self._keywords = {'Image_charge_model': 'IMAGE_CHARGE_MODEL', 'Hf_like_ev_start': 'HF_LIKE_EV_START', 'Analytic_continuation': 'ANALYTIC_CONTINUATION', 'Stop_crit': 'STOP_CRIT', 'Normalize_sigma': 'NORMALIZE_SIGMA', 'Check_fit': 'CHECK_FIT', 'Omega_max_fit': 'OMEGA_MAX_FIT', 'Neglect_normalization_sigma_x': 'NEGLECT_NORMALIZATION_SIGMA_X', 'Nparam_pade': 'NPARAM_PADE', 'Ri_sigma_x': 'RI_SIGMA_X', 'Ev_sc_iter': 'EV_SC_ITER', 'Atoms': 'ATOMS', 'Scaling': 'SCALING', 'Contour_def_end': 'CONTOUR_DEF_END', 'Crossing_search': 'CROSSING_SEARCH', 'Eps_ev_sc_iter': 'EPS_EV_SC_ITER', 'Bse': 'BSE', 'Fermi_level_offset': 'FERMI_LEVEL_OFFSET', 'Contour_def_start': 'CONTOUR_DEF_START', 'Atom_range': 'ATOM_RANGE', 'Print_gw_details': 'PRINT_GW_DETAILS', 'Periodic': 'PERIODIC', 'Ic_corr_list_beta': 'IC_CORR_LIST_BETA', 'Max_iter_fit': 'MAX_ITER_FIT', 'Mix_exchange': 'MIX_EXCHANGE', 'Eps_charge': 'EPS_CHARGE', 'Ic_corr_list': 'IC_CORR_LIST', 'Print_fit_error': 'PRINT_FIT_ERROR', 'Fraction_exx': 'FRACTION_EXX', 'Numb_poles': 'NUMB_POLES', 'Ev_sc_gw_remove_neg_virt_energies': 'EV_SC_GW_REMOVE_NEG_VIRT_ENERGIES', 'Corr_mos_virt': 'CORR_MOS_VIRT', 'Contour_def_offset': 'CONTOUR_DEF_OFFSET', 'Corr_mos_occ': 'CORR_MOS_OCC', 'Ri_metric': 'RI_METRIC'}
        self._subsections = {'BSE': 'BSE', 'IC': 'IC', 'PERIODIC': 'PERIODIC'}
        self._aliases = {'Ic': 'Image_charge_model', 'Fit_error': 'Print_fit_error', 'Cd_offset': 'Contour_def_offset', 'Remove_neg': 'Ev_sc_gw_remove_neg_virt_energies', 'Cd_start': 'Contour_def_start', 'Corr_virt': 'Corr_mos_virt', 'Corr_occ': 'Corr_mos_occ', 'Cd_end': 'Contour_def_end', 'Alpha': 'Fraction_exx', 'A_scaling': 'Scaling', 'Stop_crit_1': 'Stop_crit', 'Ri': 'Ri_metric'}


    @property
    def Corr_occ(self):
        """
        See documentation for Corr_mos_occ
        """
        return self.Corr_mos_occ

    @property
    def Corr_virt(self):
        """
        See documentation for Corr_mos_virt
        """
        return self.Corr_mos_virt

    @property
    def A_scaling(self):
        """
        See documentation for Scaling
        """
        return self.Scaling

    @property
    def Stop_crit_1(self):
        """
        See documentation for Stop_crit
        """
        return self.Stop_crit

    @property
    def Fit_error(self):
        """
        See documentation for Print_fit_error
        """
        return self.Print_fit_error

    @property
    def Remove_neg(self):
        """
        See documentation for Ev_sc_gw_remove_neg_virt_energies
        """
        return self.Ev_sc_gw_remove_neg_virt_energies

    @property
    def Ri(self):
        """
        See documentation for Ri_metric
        """
        return self.Ri_metric

    @property
    def Alpha(self):
        """
        See documentation for Fraction_exx
        """
        return self.Fraction_exx

    @property
    def Cd_start(self):
        """
        See documentation for Contour_def_start
        """
        return self.Contour_def_start

    @property
    def Cd_end(self):
        """
        See documentation for Contour_def_end
        """
        return self.Contour_def_end

    @property
    def Cd_offset(self):
        """
        See documentation for Contour_def_offset
        """
        return self.Contour_def_offset

    @property
    def Ic(self):
        """
        See documentation for Image_charge_model
        """
        return self.Image_charge_model

    @Corr_occ.setter
    def Corr_occ(self, value):
        self.Corr_mos_occ = value

    @Corr_virt.setter
    def Corr_virt(self, value):
        self.Corr_mos_virt = value

    @A_scaling.setter
    def A_scaling(self, value):
        self.Scaling = value

    @Stop_crit_1.setter
    def Stop_crit_1(self, value):
        self.Stop_crit = value

    @Fit_error.setter
    def Fit_error(self, value):
        self.Print_fit_error = value

    @Remove_neg.setter
    def Remove_neg(self, value):
        self.Ev_sc_gw_remove_neg_virt_energies = value

    @Ri.setter
    def Ri(self, value):
        self.Ri_metric = value

    @Alpha.setter
    def Alpha(self, value):
        self.Fraction_exx = value

    @Cd_start.setter
    def Cd_start(self, value):
        self.Contour_def_start = value

    @Cd_end.setter
    def Cd_end(self, value):
        self.Contour_def_end = value

    @Cd_offset.setter
    def Cd_offset(self, value):
        self.Contour_def_offset = value

    @Ic.setter
    def Ic(self, value):
        self.Image_charge_model = value
