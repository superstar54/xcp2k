from xcp2k.inputsection import InputSection


class _slab_sampling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom_list = []
        self.Range = None
        self.Length = None
        self.Surf_direction = None
        self._name = "SLAB_SAMPLING"
        self._keywords = {'Range': 'RANGE', 'Length': 'LENGTH', 'Surf_direction': 'SURF_DIRECTION'}
        self._repeated_keywords = {'Atom_list': 'ATOM_LIST'}

