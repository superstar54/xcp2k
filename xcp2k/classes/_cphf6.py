from xcp2k.inputsection import InputSection


class _cphf6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_conv = None
        self._name = "CPHF"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_conv': 'EPS_CONV'}
        self._aliases = {'Max_num_iter': 'Max_iter'}


    @property
    def Max_num_iter(self):
        """
        See documentation for Max_iter
        """
        return self.Max_iter

    @Max_num_iter.setter
    def Max_num_iter(self, value):
        self.Max_iter = value
