from xcp2k.inputsection import InputSection


class _mol_probabilities1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pmavbmc_mol = None
        self.Pmswap_mol = None
        self.Pmrot_mol = None
        self.Pmtraion_mol = None
        self.Pmtrans_mol = None
        self._name = "MOL_PROBABILITIES"
        self._keywords = {'Pmtrans_mol': 'PMTRANS_MOL', 'Pmrot_mol': 'PMROT_MOL', 'Pmswap_mol': 'PMSWAP_MOL', 'Pmavbmc_mol': 'PMAVBMC_MOL', 'Pmtraion_mol': 'PMTRAION_MOL'}

