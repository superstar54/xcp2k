from xcp2k.inputsection import InputSection


class _constraint2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Target = None
        self.Equal_charges = None
        self.Atom_list = []
        self.Atom_coef = None
        self._name = "CONSTRAINT"
        self._keywords = {'Atom_coef': 'ATOM_COEF', 'Target': 'TARGET', 'Equal_charges': 'EQUAL_CHARGES'}
        self._repeated_keywords = {'Atom_list': 'ATOM_LIST'}

