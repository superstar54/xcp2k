from xcp2k.inputsection import InputSection
from _cell_ref1 import _cell_ref1


class _cell3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.A = None
        self.B = None
        self.C = None
        self.Abc = None
        self.Alpha_beta_gamma = None
        self.Cell_file_name = None
        self.Cell_file_format = None
        self.Periodic = None
        self.Multiple_unit_cell = None
        self.Symmetry = None
        self.CELL_REF = _cell_ref1()
        self._name = "CELL"
        self._keywords = {'A': 'A', 'Cell_file_format': 'CELL_FILE_FORMAT', 'C': 'C', 'B': 'B', 'Symmetry': 'SYMMETRY', 'Alpha_beta_gamma': 'ALPHA_BETA_GAMMA', 'Multiple_unit_cell': 'MULTIPLE_UNIT_CELL', 'Periodic': 'PERIODIC', 'Abc': 'ABC', 'Cell_file_name': 'CELL_FILE_NAME'}
        self._subsections = {'CELL_REF': 'CELL_REF'}
        self._aliases = {'Angles': 'Alpha_beta_gamma'}


    @property
    def Angles(self):
        """
        See documentation for Alpha_beta_gamma
        """
        return self.Alpha_beta_gamma

    @Angles.setter
    def Angles(self, value):
        self.Alpha_beta_gamma = value
