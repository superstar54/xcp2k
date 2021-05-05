from xcp2k.inputsection import InputSection
from xcp2k.classes._scf1 import _scf1
from xcp2k.classes._ls_scf1 import _ls_scf1
from xcp2k.classes._almo_scf1 import _almo_scf1
from xcp2k.classes._kg_method1 import _kg_method1
from xcp2k.classes._energy_correction1 import _energy_correction1
from xcp2k.classes._auxiliary_density_matrix_method1 import _auxiliary_density_matrix_method1
from xcp2k.classes._qs1 import _qs1
from xcp2k.classes._tddfpt1 import _tddfpt1
from xcp2k.classes._mgrid1 import _mgrid1
from xcp2k.classes._xc4 import _xc4
from xcp2k.classes._relativistic1 import _relativistic1
from xcp2k.classes._sic2 import _sic2
from xcp2k.classes._low_spin_roks1 import _low_spin_roks1
from xcp2k.classes._efield1 import _efield1
from xcp2k.classes._periodic_efield1 import _periodic_efield1
from xcp2k.classes._external_potential2 import _external_potential2
from xcp2k.classes._transport1 import _transport1
from xcp2k.classes._external_density1 import _external_density1
from xcp2k.classes._external_vxc1 import _external_vxc1
from xcp2k.classes._poisson1 import _poisson1
from xcp2k.classes._kpoints1 import _kpoints1
from xcp2k.classes._scrf1 import _scrf1
from xcp2k.classes._density_fitting1 import _density_fitting1
from xcp2k.classes._xas1 import _xas1
from xcp2k.classes._xas_tdp1 import _xas_tdp1
from xcp2k.classes._localize10 import _localize10
from xcp2k.classes._real_time_propagation1 import _real_time_propagation1
from xcp2k.classes._print55 import _print55
from xcp2k.classes._sccs2 import _sccs2


class _dft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Basis_set_file_name = []
        self.Potential_file_name = None
        self.Wfn_restart_file_name = None
        self.Uks = None
        self.Roks = None
        self.Multiplicity = None
        self.Charge = None
        self.Excitations = None
        self.Plus_u_method = None
        self.Relax_multiplicity = None
        self.Subcells = None
        self.Auto_basis = []
        self.Surface_dipole_correction = None
        self.Surf_dip_dir = None
        self.Surf_dip_pos = None
        self.Surf_dip_switch = None
        self.Core_corr_dip = None
        self.Sort_basis = None
        self.SCF = _scf1()
        self.LS_SCF = _ls_scf1()
        self.ALMO_SCF = _almo_scf1()
        self.KG_METHOD = _kg_method1()
        self.ENERGY_CORRECTION = _energy_correction1()
        self.AUXILIARY_DENSITY_MATRIX_METHOD = _auxiliary_density_matrix_method1()
        self.QS = _qs1()
        self.TDDFPT = _tddfpt1()
        self.MGRID = _mgrid1()
        self.XC = _xc4()
        self.RELATIVISTIC = _relativistic1()
        self.SIC = _sic2()
        self.LOW_SPIN_ROKS = _low_spin_roks1()
        self.EFIELD_list = []
        self.PERIODIC_EFIELD_list = []
        self.EXTERNAL_POTENTIAL = _external_potential2()
        self.TRANSPORT = _transport1()
        self.EXTERNAL_DENSITY = _external_density1()
        self.EXTERNAL_VXC = _external_vxc1()
        self.POISSON = _poisson1()
        self.KPOINTS = _kpoints1()
        self.SCRF = _scrf1()
        self.DENSITY_FITTING = _density_fitting1()
        self.XAS = _xas1()
        self.XAS_TDP = _xas_tdp1()
        self.LOCALIZE = _localize10()
        self.REAL_TIME_PROPAGATION = _real_time_propagation1()
        self.PRINT = _print55()
        self.SCCS = _sccs2()
        self._name = "DFT"
        self._keywords = {'Potential_file_name': 'POTENTIAL_FILE_NAME', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME', 'Uks': 'UKS', 'Roks': 'ROKS', 'Multiplicity': 'MULTIPLICITY', 'Charge': 'CHARGE', 'Excitations': 'EXCITATIONS', 'Plus_u_method': 'PLUS_U_METHOD', 'Relax_multiplicity': 'RELAX_MULTIPLICITY', 'Subcells': 'SUBCELLS', 'Surface_dipole_correction': 'SURFACE_DIPOLE_CORRECTION', 'Surf_dip_dir': 'SURF_DIP_DIR', 'Surf_dip_pos': 'SURF_DIP_POS', 'Surf_dip_switch': 'SURF_DIP_SWITCH', 'Core_corr_dip': 'CORE_CORR_DIP', 'Sort_basis': 'SORT_BASIS'}
        self._repeated_keywords = {'Basis_set_file_name': 'BASIS_SET_FILE_NAME', 'Auto_basis': 'AUTO_BASIS'}
        self._subsections = {'SCF': 'SCF', 'LS_SCF': 'LS_SCF', 'ALMO_SCF': 'ALMO_SCF', 'KG_METHOD': 'KG_METHOD', 'ENERGY_CORRECTION': 'ENERGY_CORRECTION', 'AUXILIARY_DENSITY_MATRIX_METHOD': 'AUXILIARY_DENSITY_MATRIX_METHOD', 'QS': 'QS', 'TDDFPT': 'TDDFPT', 'MGRID': 'MGRID', 'XC': 'XC', 'RELATIVISTIC': 'RELATIVISTIC', 'SIC': 'SIC', 'LOW_SPIN_ROKS': 'LOW_SPIN_ROKS', 'EXTERNAL_POTENTIAL': 'EXTERNAL_POTENTIAL', 'TRANSPORT': 'TRANSPORT', 'EXTERNAL_DENSITY': 'EXTERNAL_DENSITY', 'EXTERNAL_VXC': 'EXTERNAL_VXC', 'POISSON': 'POISSON', 'KPOINTS': 'KPOINTS', 'SCRF': 'SCRF', 'DENSITY_FITTING': 'DENSITY_FITTING', 'XAS': 'XAS', 'XAS_TDP': 'XAS_TDP', 'LOCALIZE': 'LOCALIZE', 'REAL_TIME_PROPAGATION': 'REAL_TIME_PROPAGATION', 'PRINT': 'PRINT', 'SCCS': 'SCCS'}
        self._repeated_subsections = {'EFIELD': '_efield1', 'PERIODIC_EFIELD': '_periodic_efield1'}
        self._aliases = {'Restart_file_name': 'Wfn_restart_file_name', 'Unrestricted_kohn_sham': 'Uks', 'Lsd': 'Uks', 'Spin_polarized': 'Uks', 'Restricted_open_kohn_sham': 'Roks', 'Multip': 'Multiplicity', 'Relax_multip': 'Relax_multiplicity', 'Surface_dipole': 'Surface_dipole_correction', 'Surf_dip': 'Surface_dipole_correction'}
        self._attributes = ['EFIELD_list', 'PERIODIC_EFIELD_list']

    def EFIELD_add(self, section_parameters=None):
        new_section = _efield1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.EFIELD_list.append(new_section)
        return new_section

    def PERIODIC_EFIELD_add(self, section_parameters=None):
        new_section = _periodic_efield1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PERIODIC_EFIELD_list.append(new_section)
        return new_section


    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @property
    def Unrestricted_kohn_sham(self):
        """
        See documentation for Uks
        """
        return self.Uks

    @property
    def Lsd(self):
        """
        See documentation for Uks
        """
        return self.Uks

    @property
    def Spin_polarized(self):
        """
        See documentation for Uks
        """
        return self.Uks

    @property
    def Restricted_open_kohn_sham(self):
        """
        See documentation for Roks
        """
        return self.Roks

    @property
    def Multip(self):
        """
        See documentation for Multiplicity
        """
        return self.Multiplicity

    @property
    def Relax_multip(self):
        """
        See documentation for Relax_multiplicity
        """
        return self.Relax_multiplicity

    @property
    def Surface_dipole(self):
        """
        See documentation for Surface_dipole_correction
        """
        return self.Surface_dipole_correction

    @property
    def Surf_dip(self):
        """
        See documentation for Surface_dipole_correction
        """
        return self.Surface_dipole_correction

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value

    @Unrestricted_kohn_sham.setter
    def Unrestricted_kohn_sham(self, value):
        self.Uks = value

    @Lsd.setter
    def Lsd(self, value):
        self.Uks = value

    @Spin_polarized.setter
    def Spin_polarized(self, value):
        self.Uks = value

    @Restricted_open_kohn_sham.setter
    def Restricted_open_kohn_sham(self, value):
        self.Roks = value

    @Multip.setter
    def Multip(self, value):
        self.Multiplicity = value

    @Relax_multip.setter
    def Relax_multip(self, value):
        self.Relax_multiplicity = value

    @Surface_dipole.setter
    def Surface_dipole(self, value):
        self.Surface_dipole_correction = value

    @Surf_dip.setter
    def Surf_dip(self, value):
        self.Surface_dipole_correction = value
