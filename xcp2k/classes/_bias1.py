from xcp2k.inputsection import InputSection
from xcp2k.classes._print58 import _print58


class _bias1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.K_b = None
        self.Sigma_0 = None
        self.Align_nnp_energies = None
        self.PRINT = _print58()
        self._name = "BIAS"
        self._keywords = {'K_b': 'K_B', 'Sigma_0': 'SIGMA_0', 'Align_nnp_energies': 'ALIGN_NNP_ENERGIES'}
        self._subsections = {'PRINT': 'PRINT'}

