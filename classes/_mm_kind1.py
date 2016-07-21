from xcp2k.inputsection import InputSection


class _mm_kind1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Radius = None
        self.Corr_radius = None
        self._name = "MM_KIND"
        self._keywords = {'Corr_radius': 'CORR_RADIUS', 'Radius': 'RADIUS'}
        self._attributes = ['Section_parameters']

