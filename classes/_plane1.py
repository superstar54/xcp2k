from xcp2k.inputsection import InputSection


class _plane1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Def_type = None
        self.Atoms = None
        self.Normal_vector = None
        self._name = "PLANE"
        self._keywords = {'Def_type': 'DEF_TYPE', 'Normal_vector': 'NORMAL_VECTOR', 'Atoms': 'ATOMS'}

