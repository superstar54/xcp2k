from xcp2k.inputsection import InputSection


class _rdf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Maxr = None
        self.Nbin = None
        self.Solute_he = None
        self.He_he = None
        self._name = "RDF"
        self._keywords = {'Maxr': 'MAXR', 'Nbin': 'NBIN', 'Solute_he': 'SOLUTE_HE', 'He_he': 'HE_HE'}
        self._attributes = ['Section_parameters']

