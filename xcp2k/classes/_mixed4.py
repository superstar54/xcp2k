from xcp2k.inputsection import InputSection


class _mixed4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy_function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Dx = None
        self.Error_limit = None
        self._name = "MIXED"
        self._keywords = {'Energy_function': 'ENERGY_FUNCTION', 'Variables': 'VARIABLES', 'Dx': 'DX', 'Error_limit': 'ERROR_LIMIT'}
        self._repeated_keywords = {'Parameters': 'PARAMETERS', 'Values': 'VALUES', 'Units': 'UNITS'}

