from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info52 import _program_run_info52


class _ddapc_restraint_b1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type_of_density = None
        self.Strength = None
        self.Target = None
        self.Atoms = None
        self.Coeff = None
        self.Functional_form = None
        self.PROGRAM_RUN_INFO = _program_run_info52()
        self._name = "DDAPC_RESTRAINT_B"
        self._keywords = {'Type_of_density': 'TYPE_OF_DENSITY', 'Strength': 'STRENGTH', 'Target': 'TARGET', 'Atoms': 'ATOMS', 'Coeff': 'COEFF', 'Functional_form': 'FUNCTIONAL_FORM'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

