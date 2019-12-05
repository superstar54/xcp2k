from xcp2k.inputsection import InputSection
from xcp2k.classes._print58 import _print58
from xcp2k.classes._interpolator10 import _interpolator10


class _nmr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Interpolate_shift = None
        self.Nics = None
        self.Nics_file_name = None
        self.Restart_nmr = None
        self.Shift_gapw_radius = None
        self.PRINT = _print58()
        self.INTERPOLATOR = _interpolator10()
        self._name = "NMR"
        self._keywords = {'Interpolate_shift': 'INTERPOLATE_SHIFT', 'Nics': 'NICS', 'Nics_file_name': 'NICS_FILE_NAME', 'Restart_nmr': 'RESTART_NMR', 'Shift_gapw_radius': 'SHIFT_GAPW_RADIUS'}
        self._subsections = {'PRINT': 'PRINT', 'INTERPOLATOR': 'INTERPOLATOR'}
        self._attributes = ['Section_parameters']

