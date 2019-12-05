from xcp2k.inputsection import InputSection


class _generic1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mixing_function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Dx = None
        self.Error_limit = None
        self._name = "GENERIC"
        self._keywords = {'Mixing_function': 'MIXING_FUNCTION', 'Variables': 'VARIABLES', 'Dx': 'DX', 'Error_limit': 'ERROR_LIMIT'}
        self._repeated_keywords = {'Parameters': 'PARAMETERS', 'Values': 'VALUES', 'Units': 'UNITS'}

