from xcp2k.inputsection import InputSection
from _print50 import _print50
from _interpolator11 import _interpolator11


class _spinspin1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Restart_spinspin = None
        self.Issc_on_atom_list = []
        self.Do_fc = None
        self.Do_sd = None
        self.Do_pso = None
        self.Do_dso = None
        self.PRINT = _print50()
        self.INTERPOLATOR = _interpolator11()
        self._name = "SPINSPIN"
        self._keywords = {'Do_dso': 'DO_DSO', 'Do_fc': 'DO_FC', 'Restart_spinspin': 'RESTART_SPINSPIN', 'Do_sd': 'DO_SD', 'Do_pso': 'DO_PSO'}
        self._repeated_keywords = {'Issc_on_atom_list': 'ISSC_ON_ATOM_LIST'}
        self._subsections = {'PRINT': 'PRINT', 'INTERPOLATOR': 'INTERPOLATOR'}
        self._attributes = ['Section_parameters']

