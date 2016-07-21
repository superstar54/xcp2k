from xcp2k.inputsection import InputSection
from _basis1 import _basis1
from _potential2 import _potential2
from _kg_potential1 import _kg_potential1
from _dft_plus_u1 import _dft_plus_u1
from _bs1 import _bs1


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
        self.Element = None
        self.Mass = None
        self.Potential = None
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
        self.No_optimize = None
        self.Pao_basis_size = None
        self.Pao_potential_maxl = None
        self.Pao_potential_beta = None
        self.Pao_potential_neighbors = None
        self.BASIS_list = []
        self.POTENTIAL = _potential2()
        self.KG_POTENTIAL = _kg_potential1()
        self.DFT_PLUS_U = _dft_plus_u1()
        self.BS = _bs1()
        self._name = "KIND"
        self._keywords = {'Pao_potential_beta': 'PAO_POTENTIAL_BETA', 'Gpw_type': 'GPW_TYPE', 'Pao_potential_maxl': 'PAO_POTENTIAL_MAXL', 'Dftb3_param': 'DFTB3_PARAM', 'Pao_basis_size': 'PAO_BASIS_SIZE', 'Potential': 'POTENTIAL', 'Se_p_orbitals_on_h': 'SE_P_ORBITALS_ON_H', 'Elec_conf': 'ELEC_CONF', 'Core_correction': 'CORE_CORRECTION', 'Kg_potential': 'KG_POTENTIAL', 'Lmax_dftb': 'LMAX_DFTB', 'Lri_basis_set': 'LRI_BASIS_SET', 'Hard_exp_radius': 'HARD_EXP_RADIUS', 'Mao': 'MAO', 'Ghost': 'GHOST', 'Max_rad_local': 'MAX_RAD_LOCAL', 'Radial_grid': 'RADIAL_GRID', 'Aux_basis_set': 'AUX_BASIS_SET', 'Ri_aux_basis_set': 'RI_AUX_BASIS_SET', 'Pao_potential_neighbors': 'PAO_POTENTIAL_NEIGHBORS', 'No_optimize': 'NO_OPTIMIZE', 'Element': 'ELEMENT', 'Mass': 'MASS', 'Rho0_exp_radius': 'RHO0_EXP_RADIUS', 'Aux_fit_basis_set': 'AUX_FIT_BASIS_SET', 'Mm_radius': 'MM_RADIUS', 'Lebedev_grid': 'LEBEDEV_GRID'}
        self._repeated_keywords = {'Basis_set': 'BASIS_SET'}
        self._subsections = {'BS': 'BS', 'POTENTIAL': 'POTENTIAL', 'KG_POTENTIAL': 'KG_POTENTIAL', 'DFT_PLUS_U': 'DFT_PLUS_U'}
        self._repeated_subsections = {'BASIS': '_basis1'}
        self._aliases = {'Atomic_weight': 'Mass', 'Ri_aux_basis': 'Ri_aux_basis_set', 'Weight': 'Mass', 'Aux_basis': 'Aux_basis_set', 'Lri_basis': 'Lri_basis_set', 'Pot': 'Potential', 'Kg_pot': 'Kg_potential', 'Auxiliary_basis_set': 'Aux_basis_set', 'Ri_mp2_basis_set': 'Ri_aux_basis_set', 'Aux_fit_basis': 'Aux_fit_basis_set', 'Ri_rpa_basis_set': 'Ri_aux_basis_set', 'Auxiliary_fit_basis_set': 'Aux_fit_basis_set', 'Atomic_mass': 'Mass', 'Element_symbol': 'Element'}
        self._attributes = ['Section_parameters', 'BASIS_list']

    def BASIS_add(self, section_parameters=None):
        new_section = _basis1()
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
