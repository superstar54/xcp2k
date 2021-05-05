from xcp2k.inputsection import InputSection
from xcp2k.classes._variable1 import _variable1
from xcp2k.classes._force_matching1 import _force_matching1
from xcp2k.classes._history1 import _history1
from xcp2k.classes._restart16 import _restart16


class _optimize_input1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Accuracy = None
        self.Step_size = None
        self.Max_fun = None
        self.Iter_start_val = None
        self.Randomize_variables = None
        self.VARIABLE_list = []
        self.FORCE_MATCHING_list = []
        self.HISTORY = _history1()
        self.RESTART = _restart16()
        self._name = "OPTIMIZE_INPUT"
        self._keywords = {'Method': 'METHOD', 'Accuracy': 'ACCURACY', 'Step_size': 'STEP_SIZE', 'Max_fun': 'MAX_FUN', 'Iter_start_val': 'ITER_START_VAL', 'Randomize_variables': 'RANDOMIZE_VARIABLES'}
        self._subsections = {'HISTORY': 'HISTORY', 'RESTART': 'RESTART'}
        self._repeated_subsections = {'VARIABLE': '_variable1', 'FORCE_MATCHING': '_force_matching1'}
        self._attributes = ['VARIABLE_list', 'FORCE_MATCHING_list']

    def VARIABLE_add(self, section_parameters=None):
        new_section = _variable1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.VARIABLE_list.append(new_section)
        return new_section

    def FORCE_MATCHING_add(self, section_parameters=None):
        new_section = _force_matching1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_MATCHING_list.append(new_section)
        return new_section

