from xcp2k.inputsection import InputSection


class _walls1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Wall_skin = None
        self.Type = None
        self.K = None
        self._name = "WALLS"
        self._keywords = {'K': 'K', 'Type': 'TYPE', 'Wall_skin': 'WALL_SKIN'}

