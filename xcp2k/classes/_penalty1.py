from xcp2k.inputsection import InputSection


class _penalty1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Operator = None
        self.Penalty_strength = None
        self.Penalty_strength_decrease_factor = None
        self.Determinant_tolerance = None
        self.Final_determinant = None
        self.Compactification_filter_start = None
        self.Virtual_nlmos = None
        self._name = "PENALTY"
        self._keywords = {'Operator': 'OPERATOR', 'Penalty_strength': 'PENALTY_STRENGTH', 'Penalty_strength_decrease_factor': 'PENALTY_STRENGTH_DECREASE_FACTOR', 'Determinant_tolerance': 'DETERMINANT_TOLERANCE', 'Final_determinant': 'FINAL_DETERMINANT', 'Compactification_filter_start': 'COMPACTIFICATION_FILTER_START', 'Virtual_nlmos': 'VIRTUAL_NLMOS'}

