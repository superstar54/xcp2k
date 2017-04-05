from xcp2k.inputsection import InputSection
from _eri_mme1 import _eri_mme1


class _eri_mme_test1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Abc = None
        self.Nab_min = None
        self.Nrep = None
        self.Check_accuracy = None
        self.Lmax = None
        self.Zet_min = None
        self.Zet_max = None
        self.Nzet = None
        self.ERI_MME = _eri_mme1()
        self._name = "ERI_MME_TEST"
        self._keywords = {'Check_accuracy': 'CHECK_ACCURACY', 'Abc': 'ABC', 'Nab_min': 'NAB_MIN', 'Zet_min': 'ZET_MIN', 'Zet_max': 'ZET_MAX', 'Nzet': 'NZET', 'Lmax': 'LMAX', 'Nrep': 'NREP'}
        self._subsections = {'ERI_MME': 'ERI_MME'}
        self._attributes = ['Section_parameters']

