from xcp2k.inputsection import InputSection


class _averages2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Projected_area = []
        self.Projected_area_2 = []
        self.Winding_number_2 = []
        self.Moment_of_inertia = []
        self.Rdf = []
        self.Rho = []
        self.Iweight = None
        self._name = "AVERAGES"
        self._keywords = {'Iweight': 'IWEIGHT'}
        self._repeated_keywords = {'Projected_area': 'PROJECTED_AREA', 'Projected_area_2': 'PROJECTED_AREA_2', 'Winding_number_2': 'WINDING_NUMBER_2', 'Moment_of_inertia': 'MOMENT_OF_INERTIA', 'Rdf': 'RDF', 'Rho': 'RHO'}

