from xcp2k.inputsection import InputSection


class _relativistic1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Dkh_order = None
        self.Zora_type = None
        self.Transformation = None
        self.Z_cutoff = None
        self.Potential = None
        self._name = "RELATIVISTIC"
        self._keywords = {'Zora_type': 'ZORA_TYPE', 'Dkh_order': 'DKH_ORDER', 'Transformation': 'TRANSFORMATION', 'Potential': 'POTENTIAL', 'Z_cutoff': 'Z_CUTOFF', 'Method': 'METHOD'}

