from xcp2k.inputsection import InputSection


class _force5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = None
        self._name = "FORCE"
        self._default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

