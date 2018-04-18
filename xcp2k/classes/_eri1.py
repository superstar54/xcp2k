from xcp2k.inputsection import InputSection


class _eri1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Operator = None
        self.Operator_parameter = None
        self.Periodicity = None
        self.Cutoff_radius = None
        self.Eps_integral = None
        self._name = "ERI"
        self._keywords = {'Periodicity': 'PERIODICITY', 'Eps_integral': 'EPS_INTEGRAL', 'Operator': 'OPERATOR', 'Cutoff_radius': 'CUTOFF_RADIUS', 'Operator_parameter': 'OPERATOR_PARAMETER', 'Method': 'METHOD'}

