from xcp2k.inputsection import InputSection


class _maxwell1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Test_logical = None
        self.Test_real = None
        self.Test_integer = None
        self._name = "MAXWELL"
        self._keywords = {'Test_logical': 'TEST_LOGICAL', 'Test_real': 'TEST_REAL', 'Test_integer': 'TEST_INTEGER'}

