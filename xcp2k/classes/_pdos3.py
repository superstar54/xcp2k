from xcp2k.inputsection import InputSection
from xcp2k.classes._each379 import _each379
from xcp2k.classes._ldos3 import _ldos3
from xcp2k.classes._r_ldos3 import _r_ldos3


class _pdos3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Components = None
        self.Append = None
        self.Nlumo = None
        self.Out_each_mo = None
        self.EACH = _each379()
        self.LDOS_list = []
        self.R_LDOS_list = []
        self._name = "PDOS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Components': 'COMPONENTS', 'Append': 'APPEND', 'Nlumo': 'NLUMO', 'Out_each_mo': 'OUT_EACH_MO'}
        self._subsections = {'EACH': 'EACH'}
        self._repeated_subsections = {'LDOS': '_ldos3', 'R_LDOS': '_r_ldos3'}
        self._attributes = ['Section_parameters', 'LDOS_list', 'R_LDOS_list']

    def LDOS_add(self, section_parameters=None):
        new_section = _ldos3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LDOS_list.append(new_section)
        return new_section

    def R_LDOS_add(self, section_parameters=None):
        new_section = _r_ldos3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.R_LDOS_list.append(new_section)
        return new_section

