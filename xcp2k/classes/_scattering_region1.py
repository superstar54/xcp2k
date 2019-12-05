from xcp2k.inputsection import InputSection


class _scattering_region1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Molname = []
        self._name = "SCATTERING_REGION"
        self._repeated_keywords = {'List': 'LIST', 'Molname': 'MOLNAME'}

