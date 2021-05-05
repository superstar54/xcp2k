from xcp2k.inputsection import InputSection
from xcp2k.classes._ddapc_restraint_a1 import _ddapc_restraint_a1
from xcp2k.classes._ddapc_restraint_b1 import _ddapc_restraint_b1
from xcp2k.classes._projection1 import _projection1
from xcp2k.classes._program_run_info54 import _program_run_info54


class _et_coupling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type_of_constraint = None
        self.DDAPC_RESTRAINT_A_list = []
        self.DDAPC_RESTRAINT_B_list = []
        self.PROJECTION = _projection1()
        self.PROGRAM_RUN_INFO = _program_run_info54()
        self._name = "ET_COUPLING"
        self._keywords = {'Type_of_constraint': 'TYPE_OF_CONSTRAINT'}
        self._subsections = {'PROJECTION': 'PROJECTION', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}
        self._repeated_subsections = {'DDAPC_RESTRAINT_A': '_ddapc_restraint_a1', 'DDAPC_RESTRAINT_B': '_ddapc_restraint_b1'}
        self._attributes = ['DDAPC_RESTRAINT_A_list', 'DDAPC_RESTRAINT_B_list']

    def DDAPC_RESTRAINT_A_add(self, section_parameters=None):
        new_section = _ddapc_restraint_a1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DDAPC_RESTRAINT_A_list.append(new_section)
        return new_section

    def DDAPC_RESTRAINT_B_add(self, section_parameters=None):
        new_section = _ddapc_restraint_b1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DDAPC_RESTRAINT_B_list.append(new_section)
        return new_section

