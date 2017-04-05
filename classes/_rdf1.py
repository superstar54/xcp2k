from xcp2k.inputsection import InputSection


class _rdf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Maxr = None
        self.Nbin = None
        self.Centers_file_name = None
        self._name = "RDF"
        self._keywords = {'Maxr': 'MAXR', 'Nbin': 'NBIN', 'Centers_file_name': 'CENTERS_FILE_NAME'}
        self._attributes = ['Section_parameters']

