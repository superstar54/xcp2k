from xcp2k.inputsection import InputSection
from _print54 import _print54
from _interpolator13 import _interpolator13


class _polar1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Do_raman = None
        self.PRINT = _print54()
        self.INTERPOLATOR = _interpolator13()
        self._name = "POLAR"
        self._keywords = {'Do_raman': 'DO_RAMAN'}
        self._subsections = {'PRINT': 'PRINT', 'INTERPOLATOR': 'INTERPOLATOR'}
        self._attributes = ['Section_parameters']

