from xcp2k.inputsection import InputSection
from _each277 import _each277


class _xray_diffraction_spectrum1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Q_max = None
        self.EACH = _each277()
        self._name = "XRAY_DIFFRACTION_SPECTRUM"
        self._keywords = {'Q_max': 'Q_MAX', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Q_maximum': 'Q_max'}
        self._attributes = ['Section_parameters']


    @property
    def Q_maximum(self):
        """
        See documentation for Q_max
        """
        return self.Q_max

    @Q_maximum.setter
    def Q_maximum(self, value):
        self.Q_max = value
