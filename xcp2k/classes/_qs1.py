from xcp2k.inputsection import InputSection
from xcp2k.classes._distribution1 import _distribution1
from xcp2k.classes._dftb1 import _dftb1
from xcp2k.classes._se1 import _se1
from xcp2k.classes._mulliken_restraint1 import _mulliken_restraint1
from xcp2k.classes._ddapc_restraint1 import _ddapc_restraint1
from xcp2k.classes._becke_constraint1 import _becke_constraint1
from xcp2k.classes._cdft1 import _cdft1
from xcp2k.classes._s2_restraint1 import _s2_restraint1
from xcp2k.classes._lrigpw2 import _lrigpw2
from xcp2k.classes._optimize_lri_basis1 import _optimize_lri_basis1
from xcp2k.classes._opt_embed1 import _opt_embed1


class _qs1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_default = None
        self.Eps_core_charge = None
        self.Eps_gvg_rspace = None
        self.Eps_pgf_orb = None
        self.Eps_kg_orb = None
        self.Eps_ppl = None
        self.Eps_ppnl = None
        self.Eps_cpc = None
        self.Eps_rho = None
        self.Eps_rho_rspace = None
        self.Eps_rho_gspace = None
        self.Eps_filter_matrix = None
        self.Epsfit = None
        self.Epsiso = None
        self.Epssvd = None
        self.Epsrho0 = None
        self.Alpha0_hard = None
        self.Force_paw = None
        self.Max_rad_local = None
        self.Ls_scf = None
        self.Almo_scf = None
        self.Transport = None
        self.Kg_method = None
        self.Map_consistent = None
        self.Ref_embed_subsys = None
        self.Cluster_embed_subsys = None
        self.High_level_embed_subsys = None
        self.Dfet_embedded = None
        self.Lmaxn1 = None
        self.Lmaxn0 = None
        self.Laddn0 = None
        self.Quadrature = None
        self.Pw_grid = None
        self.Pw_grid_layout = None
        self.Pw_grid_blocked = None
        self.Extrapolation = None
        self.Extrapolation_order = None
        self.Method = None
        self.Core_ppl = None
        self.Embed_restart_file_name = None
        self.Embed_cube_file_name = None
        self.Embed_spin_cube_file_name = None
        self.DISTRIBUTION = _distribution1()
        self.DFTB = _dftb1()
        self.SE = _se1()
        self.MULLIKEN_RESTRAINT = _mulliken_restraint1()
        self.DDAPC_RESTRAINT_list = []
        self.BECKE_CONSTRAINT = _becke_constraint1()
        self.CDFT = _cdft1()
        self.S2_RESTRAINT = _s2_restraint1()
        self.LRIGPW = _lrigpw2()
        self.OPTIMIZE_LRI_BASIS = _optimize_lri_basis1()
        self.OPT_EMBED = _opt_embed1()
        self._name = "QS"
        self._keywords = {'Eps_default': 'EPS_DEFAULT', 'Eps_core_charge': 'EPS_CORE_CHARGE', 'Eps_gvg_rspace': 'EPS_GVG_RSPACE', 'Eps_pgf_orb': 'EPS_PGF_ORB', 'Eps_kg_orb': 'EPS_KG_ORB', 'Eps_ppl': 'EPS_PPL', 'Eps_ppnl': 'EPS_PPNL', 'Eps_cpc': 'EPS_CPC', 'Eps_rho': 'EPS_RHO', 'Eps_rho_rspace': 'EPS_RHO_RSPACE', 'Eps_rho_gspace': 'EPS_RHO_GSPACE', 'Eps_filter_matrix': 'EPS_FILTER_MATRIX', 'Epsfit': 'EPSFIT', 'Epsiso': 'EPSISO', 'Epssvd': 'EPSSVD', 'Epsrho0': 'EPSRHO0', 'Alpha0_hard': 'ALPHA0_HARD', 'Force_paw': 'FORCE_PAW', 'Max_rad_local': 'MAX_RAD_LOCAL', 'Ls_scf': 'LS_SCF', 'Almo_scf': 'ALMO_SCF', 'Transport': 'TRANSPORT', 'Kg_method': 'KG_METHOD', 'Map_consistent': 'MAP_CONSISTENT', 'Ref_embed_subsys': 'REF_EMBED_SUBSYS', 'Cluster_embed_subsys': 'CLUSTER_EMBED_SUBSYS', 'High_level_embed_subsys': 'HIGH_LEVEL_EMBED_SUBSYS', 'Dfet_embedded': 'DFET_EMBEDDED', 'Lmaxn1': 'LMAXN1', 'Lmaxn0': 'LMAXN0', 'Laddn0': 'LADDN0', 'Quadrature': 'QUADRATURE', 'Pw_grid': 'PW_GRID', 'Pw_grid_layout': 'PW_GRID_LAYOUT', 'Pw_grid_blocked': 'PW_GRID_BLOCKED', 'Extrapolation': 'EXTRAPOLATION', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Method': 'METHOD', 'Core_ppl': 'CORE_PPL', 'Embed_restart_file_name': 'EMBED_RESTART_FILE_NAME', 'Embed_cube_file_name': 'EMBED_CUBE_FILE_NAME', 'Embed_spin_cube_file_name': 'EMBED_SPIN_CUBE_FILE_NAME'}
        self._subsections = {'DISTRIBUTION': 'DISTRIBUTION', 'DFTB': 'DFTB', 'SE': 'SE', 'MULLIKEN_RESTRAINT': 'MULLIKEN_RESTRAINT', 'BECKE_CONSTRAINT': 'BECKE_CONSTRAINT', 'CDFT': 'CDFT', 'S2_RESTRAINT': 'S2_RESTRAINT', 'LRIGPW': 'LRIGPW', 'OPTIMIZE_LRI_BASIS': 'OPTIMIZE_LRI_BASIS', 'OPT_EMBED': 'OPT_EMBED'}
        self._repeated_subsections = {'DDAPC_RESTRAINT': '_ddapc_restraint1'}
        self._aliases = {'Eps_gvg': 'Eps_gvg_rspace', 'Eps_fit': 'Epsfit', 'Eps_iso': 'Epsiso', 'Eps_svd': 'Epssvd', 'Epsvrho0': 'Epsrho0', 'Eps_vrho0': 'Epsrho0', 'Alpha0_h': 'Alpha0_hard', 'Alpha0': 'Alpha0_hard', 'Lmaxrho1': 'Lmaxn1', 'Lmaxrho0': 'Lmaxn0', 'Interpolation': 'Extrapolation', 'Wf_interpolation': 'Extrapolation'}
        self._attributes = ['DDAPC_RESTRAINT_list']

    def DDAPC_RESTRAINT_add(self, section_parameters=None):
        new_section = _ddapc_restraint1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DDAPC_RESTRAINT_list.append(new_section)
        return new_section


    @property
    def Eps_gvg(self):
        """
        See documentation for Eps_gvg_rspace
        """
        return self.Eps_gvg_rspace

    @property
    def Eps_fit(self):
        """
        See documentation for Epsfit
        """
        return self.Epsfit

    @property
    def Eps_iso(self):
        """
        See documentation for Epsiso
        """
        return self.Epsiso

    @property
    def Eps_svd(self):
        """
        See documentation for Epssvd
        """
        return self.Epssvd

    @property
    def Epsvrho0(self):
        """
        See documentation for Epsrho0
        """
        return self.Epsrho0

    @property
    def Eps_vrho0(self):
        """
        See documentation for Epsrho0
        """
        return self.Epsrho0

    @property
    def Alpha0_h(self):
        """
        See documentation for Alpha0_hard
        """
        return self.Alpha0_hard

    @property
    def Alpha0(self):
        """
        See documentation for Alpha0_hard
        """
        return self.Alpha0_hard

    @property
    def Lmaxrho1(self):
        """
        See documentation for Lmaxn1
        """
        return self.Lmaxn1

    @property
    def Lmaxrho0(self):
        """
        See documentation for Lmaxn0
        """
        return self.Lmaxn0

    @property
    def Interpolation(self):
        """
        See documentation for Extrapolation
        """
        return self.Extrapolation

    @property
    def Wf_interpolation(self):
        """
        See documentation for Extrapolation
        """
        return self.Extrapolation

    @Eps_gvg.setter
    def Eps_gvg(self, value):
        self.Eps_gvg_rspace = value

    @Eps_fit.setter
    def Eps_fit(self, value):
        self.Epsfit = value

    @Eps_iso.setter
    def Eps_iso(self, value):
        self.Epsiso = value

    @Eps_svd.setter
    def Eps_svd(self, value):
        self.Epssvd = value

    @Epsvrho0.setter
    def Epsvrho0(self, value):
        self.Epsrho0 = value

    @Eps_vrho0.setter
    def Eps_vrho0(self, value):
        self.Epsrho0 = value

    @Alpha0_h.setter
    def Alpha0_h(self, value):
        self.Alpha0_hard = value

    @Alpha0.setter
    def Alpha0(self, value):
        self.Alpha0_hard = value

    @Lmaxrho1.setter
    def Lmaxrho1(self, value):
        self.Lmaxn1 = value

    @Lmaxrho0.setter
    def Lmaxrho0(self, value):
        self.Lmaxn0 = value

    @Interpolation.setter
    def Interpolation(self, value):
        self.Extrapolation = value

    @Wf_interpolation.setter
    def Wf_interpolation(self, value):
        self.Extrapolation = value
