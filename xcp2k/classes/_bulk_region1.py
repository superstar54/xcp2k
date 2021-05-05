from xcp2k.inputsection import InputSection
from xcp2k.classes._cell6 import _cell6


class _bulk_region1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Molname = []
        self.CELL_list = []
        self._name = "BULK_REGION"
        self._repeated_keywords = {'List': 'LIST', 'Molname': 'MOLNAME'}
        self._repeated_subsections = {'CELL': '_cell6'}
        self._attributes = ['CELL_list']

    def CELL_add(self, section_parameters=None):
        new_section = _cell6()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CELL_list.append(new_section)
        return new_section

