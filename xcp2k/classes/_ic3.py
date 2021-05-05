from xcp2k.inputsection import InputSection


class _ic3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Print_ic_list = None
        self.Eps_dist = None
        self._name = "IC"
        self._keywords = {'Print_ic_list': 'PRINT_IC_LIST', 'Eps_dist': 'EPS_DIST'}

