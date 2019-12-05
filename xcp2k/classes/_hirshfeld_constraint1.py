from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info17 import _program_run_info17


class _hirshfeld_constraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Strength = None
        self.Target = None
        self.Atoms = None
        self.Coeff = []
        self.Self_consistent = None
        self.Shape_function = None
        self.Reference_charge = None
        self.User_radius = None
        self.Atomic_radii = None
        self.PROGRAM_RUN_INFO = _program_run_info17()
        self._name = "HIRSHFELD_CONSTRAINT"
        self._keywords = {'Strength': 'STRENGTH', 'Target': 'TARGET', 'Atoms': 'ATOMS', 'Self_consistent': 'SELF_CONSISTENT', 'Shape_function': 'SHAPE_FUNCTION', 'Reference_charge': 'REFERENCE_CHARGE', 'User_radius': 'USER_RADIUS', 'Atomic_radii': 'ATOMIC_RADII'}
        self._repeated_keywords = {'Coeff': 'COEFF'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

