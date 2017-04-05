from xcp2k.inputsection import InputSection


class _genpot4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "GENPOT"
        self._keywords = {'Function': 'FUNCTION', 'Rmin': 'RMIN', 'Variables': 'VARIABLES', 'Rmax': 'RMAX', 'Rcut': 'RCUT', 'Atoms': 'ATOMS'}
        self._repeated_keywords = {'Units': 'UNITS', 'Values': 'VALUES', 'Parameters': 'PARAMETERS'}

