from xcp2k.inputsection import InputSection


class _mulliken_restraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Strength = None
        self.Target = None
        self.Atoms = None
        self._name = "MULLIKEN_RESTRAINT"
        self._keywords = {'Strength': 'STRENGTH', 'Target': 'TARGET', 'Atoms': 'ATOMS'}

