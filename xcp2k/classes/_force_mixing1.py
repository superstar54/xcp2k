from xcp2k.inputsection import InputSection
from xcp2k.classes._qm_non_adaptive1 import _qm_non_adaptive1
from xcp2k.classes._buffer_non_adaptive1 import _buffer_non_adaptive1
from xcp2k.classes._buffer_links1 import _buffer_links1
from xcp2k.classes._restart_info1 import _restart_info1
from xcp2k.classes._print45 import _print45


class _force_mixing1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Momentum_conservation_type = None
        self.Momentum_conservation_region = None
        self.R_core = None
        self.R_qm = None
        self.Qm_extended_seed_is_only_core_list = None
        self.R_buf = None
        self.Qm_kind_element_mapping = []
        self.Max_n_qm = None
        self.Adaptive_exclude_molecules = None
        self.Extended_delta_charge = None
        self.QM_NON_ADAPTIVE_list = []
        self.BUFFER_NON_ADAPTIVE_list = []
        self.BUFFER_LINKS_list = []
        self.RESTART_INFO = _restart_info1()
        self.PRINT = _print45()
        self._name = "FORCE_MIXING"
        self._keywords = {'Momentum_conservation_type': 'MOMENTUM_CONSERVATION_TYPE', 'Momentum_conservation_region': 'MOMENTUM_CONSERVATION_REGION', 'R_core': 'R_CORE', 'R_qm': 'R_QM', 'Qm_extended_seed_is_only_core_list': 'QM_EXTENDED_SEED_IS_ONLY_CORE_LIST', 'R_buf': 'R_BUF', 'Max_n_qm': 'MAX_N_QM', 'Adaptive_exclude_molecules': 'ADAPTIVE_EXCLUDE_MOLECULES', 'Extended_delta_charge': 'EXTENDED_DELTA_CHARGE'}
        self._repeated_keywords = {'Qm_kind_element_mapping': 'QM_KIND_ELEMENT_MAPPING'}
        self._subsections = {'RESTART_INFO': 'RESTART_INFO', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'QM_NON_ADAPTIVE': '_qm_non_adaptive1', 'BUFFER_NON_ADAPTIVE': '_buffer_non_adaptive1', 'BUFFER_LINKS': '_buffer_links1'}
        self._attributes = ['Section_parameters', 'QM_NON_ADAPTIVE_list', 'BUFFER_NON_ADAPTIVE_list', 'BUFFER_LINKS_list']

    def QM_NON_ADAPTIVE_add(self, section_parameters=None):
        new_section = _qm_non_adaptive1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QM_NON_ADAPTIVE_list.append(new_section)
        return new_section

    def BUFFER_NON_ADAPTIVE_add(self, section_parameters=None):
        new_section = _buffer_non_adaptive1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BUFFER_NON_ADAPTIVE_list.append(new_section)
        return new_section

    def BUFFER_LINKS_add(self, section_parameters=None):
        new_section = _buffer_links1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BUFFER_LINKS_list.append(new_section)
        return new_section

