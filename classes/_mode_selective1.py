from xcp2k.inputsection import InputSection
from _involved_atoms1 import _involved_atoms1
from _print59 import _print59


class _mode_selective1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Frequency = None
        self.Range = None
        self.Atoms = None
        self.Eps_max_val = None
        self.Eps_norm = None
        self.Initial_guess = None
        self.Restart_file_name = None
        self.INVOLVED_ATOMS = _involved_atoms1()
        self.PRINT_list = []
        self._name = "MODE_SELECTIVE"
        self._keywords = {'Restart_file_name': 'RESTART_FILE_NAME', 'Eps_max_val': 'EPS_MAX_VAL', 'Initial_guess': 'INITIAL_GUESS', 'Atoms': 'ATOMS', 'Range': 'RANGE', 'Frequency': 'FREQUENCY', 'Eps_norm': 'EPS_NORM'}
        self._subsections = {'INVOLVED_ATOMS': 'INVOLVED_ATOMS'}
        self._repeated_subsections = {'PRINT': '_print59'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print59()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

