from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info53 import _program_run_info53
from xcp2k.classes._block1 import _block1
from xcp2k.classes._print84 import _print84


class _projection1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info53()
        self.BLOCK_list = []
        self.PRINT = _print84()
        self._name = "PROJECTION"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'BLOCK': '_block1'}
        self._attributes = ['BLOCK_list']

    def BLOCK_add(self, section_parameters=None):
        new_section = _block1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BLOCK_list.append(new_section)
        return new_section

