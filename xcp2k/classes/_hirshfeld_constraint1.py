from xcp2k.inputsection import InputSection
from _program_run_info16 import _program_run_info16


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
        self.PROGRAM_RUN_INFO = _program_run_info16()
        self._name = "HIRSHFELD_CONSTRAINT"
        self._keywords = {'Reference_charge': 'REFERENCE_CHARGE', 'Strength': 'STRENGTH', 'Target': 'TARGET', 'Shape_function': 'SHAPE_FUNCTION', 'Atoms': 'ATOMS', 'Atomic_radii': 'ATOMIC_RADII', 'Self_consistent': 'SELF_CONSISTENT', 'User_radius': 'USER_RADIUS'}
        self._repeated_keywords = {'Coeff': 'COEFF'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

