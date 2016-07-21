from xcp2k.inputsection import InputSection


class _box_probabilities1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pmhmc_box = None
        self.Pmvol_box = None
        self._name = "BOX_PROBABILITIES"
        self._keywords = {'Pmhmc_box': 'PMHMC_BOX', 'Pmvol_box': 'PMVOL_BOX'}

