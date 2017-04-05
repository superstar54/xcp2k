from xcp2k.inputsection import InputSection


class _charge1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom = None
        self.Charge = None
        self._name = "CHARGE"
        self._keywords = {'Charge': 'CHARGE', 'Atom': 'ATOM'}

