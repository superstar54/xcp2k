from xcp2k.inputsection import InputSection


class _matrix_iterate1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_target_factor = None
        self.Eps_lanczos = None
        self.Order_lanczos = None
        self.Max_iter_lanczos = None
        self._name = "MATRIX_ITERATE"
        self._keywords = {'Eps_target_factor': 'EPS_TARGET_FACTOR', 'Eps_lanczos': 'EPS_LANCZOS', 'Order_lanczos': 'ORDER_LANCZOS', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS'}

