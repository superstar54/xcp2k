from xcp2k.inputsection import InputSection
from xcp2k.classes._eri_mme1 import _eri_mme1


class _eri_mme_test1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Test_3c = None
        self.Test_2c = None
        self.Abc = None
        self.Min_npos = None
        self.Nrep = None
        self.Check_2c_accuracy = None
        self.Lmax = None
        self.Zet_min = None
        self.Zet_max = None
        self.Nzet = None
        self.Nsample_3c = None
        self.ERI_MME = _eri_mme1()
        self._name = "ERI_MME_TEST"
        self._keywords = {'Test_3c': 'TEST_3C', 'Test_2c': 'TEST_2C', 'Abc': 'ABC', 'Min_npos': 'MIN_NPOS', 'Nrep': 'NREP', 'Check_2c_accuracy': 'CHECK_2C_ACCURACY', 'Lmax': 'LMAX', 'Zet_min': 'ZET_MIN', 'Zet_max': 'ZET_MAX', 'Nzet': 'NZET', 'Nsample_3c': 'NSAMPLE_3C'}
        self._subsections = {'ERI_MME': 'ERI_MME'}
        self._attributes = ['Section_parameters']

