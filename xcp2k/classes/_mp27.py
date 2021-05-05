from xcp2k.inputsection import InputSection
from xcp2k.classes._mp2_info7 import _mp2_info7


class _mp27(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Method = None
        self.Big_send = None
        self.MP2_INFO = _mp2_info7()
        self._name = "MP2"
        self._keywords = {'Method': 'METHOD', 'Big_send': 'BIG_SEND'}
        self._subsections = {'MP2_INFO': 'MP2_INFO'}
        self._attributes = ['Section_parameters']

