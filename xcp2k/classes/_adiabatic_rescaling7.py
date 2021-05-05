from xcp2k.inputsection import InputSection


class _adiabatic_rescaling7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Functional_type = None
        self.Lambda = None
        self.Omega = None
        self.Functional_model = None
        self._name = "ADIABATIC_RESCALING"
        self._keywords = {'Functional_type': 'FUNCTIONAL_TYPE', 'Lambda': 'LAMBDA', 'Omega': 'OMEGA', 'Functional_model': 'FUNCTIONAL_MODEL'}

