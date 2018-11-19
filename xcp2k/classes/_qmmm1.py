from xcp2k.inputsection import InputSection
from _force_mixing1 import _force_mixing1
from _qm_kind3 import _qm_kind3
from _mm_kind1 import _mm_kind1
from _cell3 import _cell3
from _periodic13 import _periodic13
from _link3 import _link3
from _interpolator8 import _interpolator8
from _forcefield2 import _forcefield2
from _walls1 import _walls1
from _image_charge1 import _image_charge1
from _print47 import _print47


class _qmmm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.E_coupl = None
        self.Mm_potential_file_name = None
        self.Use_geep_lib = None
        self.Nocompatibility = None
        self.Eps_mm_rspace = None
        self.Spherical_cutoff = None
        self.Parallel_scheme = None
        self.Center = None
        self.Center_type = None
        self.Center_grid = None
        self.Initial_translation_vector = None
        self.Delta_charge = None
        self.FORCE_MIXING = _force_mixing1()
        self.QM_KIND_list = []
        self.MM_KIND_list = []
        self.CELL = _cell3()
        self.PERIODIC = _periodic13()
        self.LINK_list = []
        self.INTERPOLATOR = _interpolator8()
        self.FORCEFIELD_list = []
        self.WALLS = _walls1()
        self.IMAGE_CHARGE = _image_charge1()
        self.PRINT = _print47()
        self._name = "QMMM"
        self._keywords = {'Initial_translation_vector': 'INITIAL_TRANSLATION_VECTOR', 'Center': 'CENTER', 'Eps_mm_rspace': 'EPS_MM_RSPACE', 'Nocompatibility': 'NOCOMPATIBILITY', 'Use_geep_lib': 'USE_GEEP_LIB', 'Center_type': 'CENTER_TYPE', 'Parallel_scheme': 'PARALLEL_SCHEME', 'Spherical_cutoff': 'SPHERICAL_CUTOFF', 'E_coupl': 'E_COUPL', 'Center_grid': 'CENTER_GRID', 'Mm_potential_file_name': 'MM_POTENTIAL_FILE_NAME', 'Delta_charge': 'DELTA_CHARGE'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'FORCE_MIXING': 'FORCE_MIXING', 'CELL': 'CELL', 'WALLS': 'WALLS', 'PERIODIC': 'PERIODIC', 'PRINT': 'PRINT', 'IMAGE_CHARGE': 'IMAGE_CHARGE'}
        self._repeated_subsections = {'QM_KIND': '_qm_kind3', 'LINK': '_link3', 'MM_KIND': '_mm_kind1', 'FORCEFIELD': '_forcefield2'}
        self._aliases = {'Ecoupl': 'E_coupl', 'Qmmm_coupling': 'E_coupl'}
        self._attributes = ['QM_KIND_list', 'MM_KIND_list', 'LINK_list', 'FORCEFIELD_list']

    def QM_KIND_add(self, section_parameters=None):
        new_section = _qm_kind3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QM_KIND_list.append(new_section)
        return new_section

    def LINK_add(self, section_parameters=None):
        new_section = _link3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LINK_list.append(new_section)
        return new_section

    def MM_KIND_add(self, section_parameters=None):
        new_section = _mm_kind1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MM_KIND_list.append(new_section)
        return new_section

    def FORCEFIELD_add(self, section_parameters=None):
        new_section = _forcefield2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCEFIELD_list.append(new_section)
        return new_section


    @property
    def Qmmm_coupling(self):
        """
        See documentation for E_coupl
        """
        return self.E_coupl

    @property
    def Ecoupl(self):
        """
        See documentation for E_coupl
        """
        return self.E_coupl

    @Qmmm_coupling.setter
    def Qmmm_coupling(self, value):
        self.E_coupl = value

    @Ecoupl.setter
    def Ecoupl(self, value):
        self.E_coupl = value
