from xcp2k.inputsection import InputSection
from xcp2k.classes._eri_mme9 import _eri_mme9
from xcp2k.classes._wfc_gpw7 import _wfc_gpw7
from xcp2k.classes._interaction_potential21 import _interaction_potential21


class _integrals7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eri_method = None
        self.Size_lattice_sum = None
        self.ERI_MME = _eri_mme9()
        self.WFC_GPW = _wfc_gpw7()
        self.INTERACTION_POTENTIAL = _interaction_potential21()
        self._name = "INTEGRALS"
        self._keywords = {'Eri_method': 'ERI_METHOD', 'Size_lattice_sum': 'SIZE_LATTICE_SUM'}
        self._subsections = {'ERI_MME': 'ERI_MME', 'WFC_GPW': 'WFC_GPW', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL'}

