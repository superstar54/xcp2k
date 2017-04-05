from xcp2k.inputsection import InputSection


class _coulomb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Cutoff = None
        self.Rc_taper = None
        self.Rc_range = None
        self._name = "COULOMB"
        self._keywords = {'Cutoff': 'CUTOFF', 'Rc_taper': 'RC_TAPER', 'Rc_range': 'RC_RANGE'}

