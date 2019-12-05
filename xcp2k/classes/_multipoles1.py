from xcp2k.inputsection import InputSection


class _multipoles1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_multipole_expansion = None
        self.Pol_scf = None
        self.Max_ipol_iter = None
        self.Eps_pol = None
        self._name = "MULTIPOLES"
        self._keywords = {'Max_multipole_expansion': 'MAX_MULTIPOLE_EXPANSION', 'Pol_scf': 'POL_SCF', 'Max_ipol_iter': 'MAX_IPOL_ITER', 'Eps_pol': 'EPS_POL'}
        self._attributes = ['Section_parameters']

