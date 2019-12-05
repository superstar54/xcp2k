from xcp2k.inputsection import InputSection


class _external_potential2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Function = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Static = None
        self.Dx = None
        self.Error_limit = None
        self.Read_from_cube = None
        self.Scaling_factor = None
        self._name = "EXTERNAL_POTENTIAL"
        self._keywords = {'Function': 'FUNCTION', 'Static': 'STATIC', 'Dx': 'DX', 'Error_limit': 'ERROR_LIMIT', 'Read_from_cube': 'READ_FROM_CUBE', 'Scaling_factor': 'SCALING_FACTOR'}
        self._repeated_keywords = {'Parameters': 'PARAMETERS', 'Values': 'VALUES', 'Units': 'UNITS'}

