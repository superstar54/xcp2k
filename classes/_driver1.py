from xcp2k.inputsection import InputSection


class _driver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Unix = None
        self.Port = None
        self.Host = None
        self._name = "DRIVER"
        self._keywords = {'Unix': 'UNIX', 'Host': 'HOST', 'Port': 'PORT'}

