from xcp2k.inputsection import InputSection


class _thermostat_energy5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = []
        self._name = "THERMOSTAT_ENERGY"
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

