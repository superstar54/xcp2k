from xcp2k.inputsection import InputSection
from xcp2k.classes._pao_potential1 import _pao_potential1
from xcp2k.classes._pao_descriptor1 import _pao_descriptor1
from xcp2k.classes._basis2 import _basis2
from xcp2k.classes._potential2 import _potential2
from xcp2k.classes._kg_potential1 import _kg_potential1
from xcp2k.classes._dft_plus_u1 import _dft_plus_u1
from xcp2k.classes._bs1 import _bs1


class _kind1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Basis_set = []
        self.Aux_basis_set = None
        self.Ri_aux_basis_set = None
        self.Lri_basis_set = None
        self.Aux_fit_basis_set = None
        self.Elec_conf = None
        self.Core_correction = None
        self.Magnetization = None
        self.Element = None
        self.Mass = None
        self.Potential_file_name = None
        self.Potential_type = None
        self.Potential = None
        self.Kg_potential_file_name = None
        self.Kg_potential = None
        self.Hard_exp_radius = None
        self.Max_rad_local = None
        self.Rho0_exp_radius = None
        self.Lebedev_grid = None
        self.Radial_grid = None
        self.Mm_radius = None
        self.Dftb3_param = None
        self.Lmax_dftb = None
        self.Mao = None
        self.Se_p_orbitals_on_h = None
        self.Gpw_type = None
        self.Ghost = None
        self.Floating_basis_center = None
        self.No_optimize = None
        self.Pao_basis_size = None
        self.PAO_POTENTIAL_list = []
        self.PAO_DESCRIPTOR_list = []
        self.BASIS_list = []
        self.POTENTIAL = _potential2()
        self.KG_POTENTIAL = _kg_potential1()
        self.DFT_PLUS_U = _dft_plus_u1()
        self.BS = _bs1()
        self._name = "KIND"
        self._keywords = {'Aux_basis_set': 'AUX_BASIS_SET', 'Ri_aux_basis_set': 'RI_AUX_BASIS_SET', 'Lri_basis_set': 'LRI_BASIS_SET', 'Aux_fit_basis_set': 'AUX_FIT_BASIS_SET', 'Elec_conf': 'ELEC_CONF', 'Core_correction': 'CORE_CORRECTION', 'Magnetization': 'MAGNETIZATION', 'Element': 'ELEMENT', 'Mass': 'MASS', 'Potential_file_name': 'POTENTIAL_FILE_NAME', 'Potential_type': 'POTENTIAL_TYPE', 'Potential': 'POTENTIAL', 'Kg_potential_file_name': 'KG_POTENTIAL_FILE_NAME', 'Kg_potential': 'KG_POTENTIAL', 'Hard_exp_radius': 'HARD_EXP_RADIUS', 'Max_rad_local': 'MAX_RAD_LOCAL', 'Rho0_exp_radius': 'RHO0_EXP_RADIUS', 'Lebedev_grid': 'LEBEDEV_GRID', 'Radial_grid': 'RADIAL_GRID', 'Mm_radius': 'MM_RADIUS', 'Dftb3_param': 'DFTB3_PARAM', 'Lmax_dftb': 'LMAX_DFTB', 'Mao': 'MAO', 'Se_p_orbitals_on_h': 'SE_P_ORBITALS_ON_H', 'Gpw_type': 'GPW_TYPE', 'Ghost': 'GHOST', 'Floating_basis_center': 'FLOATING_BASIS_CENTER', 'No_optimize': 'NO_OPTIMIZE', 'Pao_basis_size': 'PAO_BASIS_SIZE'}
        self._repeated_keywords = {'Basis_set': 'BASIS_SET'}
        self._subsections = {'POTENTIAL': 'POTENTIAL', 'KG_POTENTIAL': 'KG_POTENTIAL', 'DFT_PLUS_U': 'DFT_PLUS_U', 'BS': 'BS'}
        self._repeated_subsections = {'PAO_POTENTIAL': '_pao_potential1', 'PAO_DESCRIPTOR': '_pao_descriptor1', 'BASIS': '_basis2'}
        self._aliases = {'Auxiliary_basis_set': 'Aux_basis_set', 'Aux_basis': 'Aux_basis_set', 'Ri_mp2_basis_set': 'Ri_aux_basis_set', 'Ri_rpa_basis_set': 'Ri_aux_basis_set', 'Ri_aux_basis': 'Ri_aux_basis_set', 'Lri_basis': 'Lri_basis_set', 'Auxiliary_fit_basis_set': 'Aux_fit_basis_set', 'Aux_fit_basis': 'Aux_fit_basis_set', 'Element_symbol': 'Element', 'Atomic_mass': 'Mass', 'Atomic_weight': 'Mass', 'Weight': 'Mass', 'Pot': 'Potential', 'Kg_pot': 'Kg_potential'}
        self._attributes = ['Section_parameters', 'PAO_POTENTIAL_list', 'PAO_DESCRIPTOR_list', 'BASIS_list']

    def PAO_POTENTIAL_add(self, section_parameters=None):
        new_section = _pao_potential1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PAO_POTENTIAL_list.append(new_section)
        return new_section

    def PAO_DESCRIPTOR_add(self, section_parameters=None):
        new_section = _pao_descriptor1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PAO_DESCRIPTOR_list.append(new_section)
        return new_section

    def BASIS_add(self, section_parameters=None):
        new_section = _basis2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BASIS_list.append(new_section)
        return new_section


    @property
    def Auxiliary_basis_set(self):
        """
        See documentation for Aux_basis_set
        """
        return self.Aux_basis_set

    @property
    def Aux_basis(self):
        """
        See documentation for Aux_basis_set
        """
        return self.Aux_basis_set

    @property
    def Ri_mp2_basis_set(self):
        """
        See documentation for Ri_aux_basis_set
        """
        return self.Ri_aux_basis_set

    @property
    def Ri_rpa_basis_set(self):
        """
        See documentation for Ri_aux_basis_set
        """
        return self.Ri_aux_basis_set

    @property
    def Ri_aux_basis(self):
        """
        See documentation for Ri_aux_basis_set
        """
        return self.Ri_aux_basis_set

    @property
    def Lri_basis(self):
        """
        See documentation for Lri_basis_set
        """
        return self.Lri_basis_set

    @property
    def Auxiliary_fit_basis_set(self):
        """
        See documentation for Aux_fit_basis_set
        """
        return self.Aux_fit_basis_set

    @property
    def Aux_fit_basis(self):
        """
        See documentation for Aux_fit_basis_set
        """
        return self.Aux_fit_basis_set

    @property
    def Element_symbol(self):
        """
        See documentation for Element
        """
        return self.Element

    @property
    def Atomic_mass(self):
        """
        See documentation for Mass
        """
        return self.Mass

    @property
    def Atomic_weight(self):
        """
        See documentation for Mass
        """
        return self.Mass

    @property
    def Weight(self):
        """
        See documentation for Mass
        """
        return self.Mass

    @property
    def Pot(self):
        """
        See documentation for Potential
        """
        return self.Potential

    @property
    def Kg_pot(self):
        """
        See documentation for Kg_potential
        """
        return self.Kg_potential

    @Auxiliary_basis_set.setter
    def Auxiliary_basis_set(self, value):
        self.Aux_basis_set = value

    @Aux_basis.setter
    def Aux_basis(self, value):
        self.Aux_basis_set = value

    @Ri_mp2_basis_set.setter
    def Ri_mp2_basis_set(self, value):
        self.Ri_aux_basis_set = value

    @Ri_rpa_basis_set.setter
    def Ri_rpa_basis_set(self, value):
        self.Ri_aux_basis_set = value

    @Ri_aux_basis.setter
    def Ri_aux_basis(self, value):
        self.Ri_aux_basis_set = value

    @Lri_basis.setter
    def Lri_basis(self, value):
        self.Lri_basis_set = value

    @Auxiliary_fit_basis_set.setter
    def Auxiliary_fit_basis_set(self, value):
        self.Aux_fit_basis_set = value

    @Aux_fit_basis.setter
    def Aux_fit_basis(self, value):
        self.Aux_fit_basis_set = value

    @Element_symbol.setter
    def Element_symbol(self, value):
        self.Element = value

    @Atomic_mass.setter
    def Atomic_mass(self, value):
        self.Mass = value

    @Atomic_weight.setter
    def Atomic_weight(self, value):
        self.Mass = value

    @Weight.setter
    def Weight(self, value):
        self.Mass = value

    @Pot.setter
    def Pot(self, value):
        self.Potential = value

    @Kg_pot.setter
    def Kg_pot(self, value):
        self.Kg_potential = value
