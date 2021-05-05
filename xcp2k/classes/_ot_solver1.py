from xcp2k.inputsection import InputSection


class _ot_solver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_iter = None
        self.Eps_iter = None
        self.Minimizer = None
        self._name = "OT_SOLVER"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_iter': 'EPS_ITER', 'Minimizer': 'MINIMIZER'}
        self._attributes = ['Section_parameters']

