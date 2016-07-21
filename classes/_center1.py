from xcp2k.inputsection import InputSection


class _center1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Xyz = None
        self.Atom_list = None
        self.Weight_type = None
        self.Fixed = None
        self._name = "CENTER"
        self._keywords = {'Fixed': 'FIXED', 'Xyz': 'XYZ', 'Atom_list': 'ATOM_LIST', 'Weight_type': 'WEIGHT_TYPE'}

