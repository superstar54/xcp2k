from xcp2k.inputsection import InputSection


class _torsion2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Atoms = []
        self._name = "TORSION"
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._attributes = ['Section_parameters']

