from xcp2k.inputsection import InputSection


class _ke_libxc6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Functional = None
        self.Scale = None
        self.Parameters = None
        self._name = "KE_LIBXC"
        self._keywords = {'Scale': 'SCALE', 'Functional': 'FUNCTIONAL', 'Parameters': 'PARAMETERS'}
        self._attributes = ['Section_parameters']

