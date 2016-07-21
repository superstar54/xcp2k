from xcp2k.inputsection import InputSection


class _variable1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Value = None
        self.Fixed = None
        self.Label = None
        self._name = "VARIABLE"
        self._keywords = {'Fixed': 'FIXED', 'Value': 'VALUE', 'Label': 'LABEL'}

