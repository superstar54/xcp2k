from xcp2k.inputsection import InputSection
from _mol_probabilities1 import _mol_probabilities1
from _box_probabilities1 import _box_probabilities1


class _move_probabilities1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pmhmc = None
        self.Pmtrans = None
        self.Pmavbmc = None
        self.Pmtraion = None
        self.Pmswap = None
        self.Pmvolume = None
        self.MOL_PROBABILITIES = _mol_probabilities1()
        self.BOX_PROBABILITIES = _box_probabilities1()
        self._name = "MOVE_PROBABILITIES"
        self._keywords = {'Pmavbmc': 'PMAVBMC', 'Pmswap': 'PMSWAP', 'Pmtraion': 'PMTRAION', 'Pmtrans': 'PMTRANS', 'Pmvolume': 'PMVOLUME', 'Pmhmc': 'PMHMC'}
        self._subsections = {'BOX_PROBABILITIES': 'BOX_PROBABILITIES', 'MOL_PROBABILITIES': 'MOL_PROBABILITIES'}

