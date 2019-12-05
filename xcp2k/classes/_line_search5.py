from xcp2k.inputsection import InputSection
from xcp2k.classes._print22 import _print22


class _line_search5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Initial_step_size = None
        self.Max_step_size = None
        self.Tiny_step_size = None
        self.Eps_step_size = None
        self.PRINT_list = []
        self._name = "LINE_SEARCH"
        self._keywords = {'Method': 'METHOD', 'Initial_step_size': 'INITIAL_STEP_SIZE', 'Max_step_size': 'MAX_STEP_SIZE', 'Tiny_step_size': 'TINY_STEP_SIZE', 'Eps_step_size': 'EPS_STEP_SIZE'}
        self._repeated_subsections = {'PRINT': '_print22'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print22()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

