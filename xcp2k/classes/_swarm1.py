from xcp2k.inputsection import InputSection
from _print69 import _print69
from _global_opt1 import _global_opt1


class _swarm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Behavior = None
        self.Number_of_workers = None
        self.Replay_communication_log = None
        self.Max_iter = None
        self.PRINT_list = []
        self.GLOBAL_OPT = _global_opt1()
        self._name = "SWARM"
        self._keywords = {'Number_of_workers': 'NUMBER_OF_WORKERS', 'Max_iter': 'MAX_ITER', 'Behavior': 'BEHAVIOR', 'Replay_communication_log': 'REPLAY_COMMUNICATION_LOG'}
        self._subsections = {'GLOBAL_OPT': 'GLOBAL_OPT'}
        self._repeated_subsections = {'PRINT': '_print69'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print69()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

