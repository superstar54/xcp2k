from xcp2k.inputsection import InputSection


class _external_potential1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_list = []
        self.Function = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Dx = None
        self.Error_limit = None
        self._name = "EXTERNAL_POTENTIAL"
        self._keywords = {'Function': 'FUNCTION', 'Dx': 'DX', 'Error_limit': 'ERROR_LIMIT'}
        self._repeated_keywords = {'Atoms_list': 'ATOMS_LIST', 'Parameters': 'PARAMETERS', 'Values': 'VALUES', 'Units': 'UNITS'}

