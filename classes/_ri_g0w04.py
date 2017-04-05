from xcp2k.inputsection import InputSection


class _ri_g0w04(InputSection):
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
        self.Cutoff_radius = None
        self.Truncation = None
        self.Ev_sc_iter = None
        self.Hf_like_ev_start = None
        self.Print_gw_details = None
        self.Contour_def_start = None
        self.Contour_def_end = None
        self.Contour_def_offset = None
        self._name = "RI_G0W0"
        self._keywords = {'Hf_like_ev_start': 'HF_LIKE_EV_START', 'Print_fit_error': 'PRINT_FIT_ERROR', 'Corr_mos_occ': 'CORR_MOS_OCC', 'Contour_def_offset': 'CONTOUR_DEF_OFFSET', 'Ev_sc_iter': 'EV_SC_ITER', 'Contour_def_start': 'CONTOUR_DEF_START', 'Scaling': 'SCALING', 'Print_gw_details': 'PRINT_GW_DETAILS', 'Corr_mos_virt': 'CORR_MOS_VIRT', 'Crossing_search': 'CROSSING_SEARCH', 'Contour_def_end': 'CONTOUR_DEF_END', 'Stop_crit': 'STOP_CRIT', 'Max_iter_fit': 'MAX_ITER_FIT', 'Cutoff_radius': 'CUTOFF_RADIUS', 'Truncation': 'TRUNCATION', 'Numb_poles': 'NUMB_POLES', 'Check_fit': 'CHECK_FIT', 'Fermi_level_offset': 'FERMI_LEVEL_OFFSET', 'Omega_max_fit': 'OMEGA_MAX_FIT'}
        self._aliases = {'Fit_error': 'Print_fit_error', 'Cd_offset': 'Contour_def_offset', 'Cd_start': 'Contour_def_start', 'Corr_virt': 'Corr_mos_virt', 'Corr_occ': 'Corr_mos_occ', 'Cd_end': 'Contour_def_end', 'A_scaling': 'Scaling', 'Stop_crit_1': 'Stop_crit'}


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

    @Cd_start.setter
    def Cd_start(self, value):
        self.Contour_def_start = value

    @Cd_end.setter
    def Cd_end(self, value):
        self.Contour_def_end = value

    @Cd_offset.setter
    def Cd_offset(self, value):
        self.Contour_def_offset = value
