from xcp2k.inputsection import InputSection
from _dielec_aa_cuboidal2 import _dielec_aa_cuboidal2
from _dielec_xaa_annular2 import _dielec_xaa_annular2


class _dielectric2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dielectric_core_correction = None
        self.Dielectric_function_type = None
        self.Dielectric_constant = None
        self.Rho_min = None
        self.Rho_max = None
        self.Derivative_method = None
        self.DIELEC_AA_CUBOIDAL_list = []
        self.DIELEC_XAA_ANNULAR_list = []
        self._name = "DIELECTRIC"
        self._keywords = {'Rho_min': 'RHO_MIN', 'Derivative_method': 'DERIVATIVE_METHOD', 'Dielectric_core_correction': 'DIELECTRIC_CORE_CORRECTION', 'Dielectric_function_type': 'DIELECTRIC_FUNCTION_TYPE', 'Rho_max': 'RHO_MAX', 'Dielectric_constant': 'DIELECTRIC_CONSTANT'}
        self._repeated_subsections = {'DIELEC_AA_CUBOIDAL': '_dielec_aa_cuboidal2', 'DIELEC_XAA_ANNULAR': '_dielec_xaa_annular2'}
        self._aliases = {'Epsilon': 'Dielectric_constant'}
        self._attributes = ['DIELEC_AA_CUBOIDAL_list', 'DIELEC_XAA_ANNULAR_list']

    def DIELEC_AA_CUBOIDAL_add(self, section_parameters=None):
        new_section = _dielec_aa_cuboidal2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DIELEC_AA_CUBOIDAL_list.append(new_section)
        return new_section

    def DIELEC_XAA_ANNULAR_add(self, section_parameters=None):
        new_section = _dielec_xaa_annular2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DIELEC_XAA_ANNULAR_list.append(new_section)
        return new_section


    @property
    def Epsilon(self):
        """
        See documentation for Dielectric_constant
        """
        return self.Dielectric_constant

    @Epsilon.setter
    def Epsilon(self, value):
        self.Dielectric_constant = value
