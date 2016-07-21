from xcp2k.inputsection import InputSection
from _program_run_info14 import _program_run_info14


class _becke_restraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Strength = None
        self.Target = None
        self.Atoms = None
        self.Coeff = None
        self.Functional_form = None
        self.Type_of_density = None
        self.PROGRAM_RUN_INFO = _program_run_info14()
        self._name = "BECKE_RESTRAINT"
        self._keywords = {'Strength': 'STRENGTH', 'Target': 'TARGET', 'Coeff': 'COEFF', 'Atoms': 'ATOMS', 'Type_of_density': 'TYPE_OF_DENSITY', 'Functional_form': 'FUNCTIONAL_FORM'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

