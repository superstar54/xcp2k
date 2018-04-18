from xcp2k.inputsection import InputSection
from _print55 import _print55
from _interpolator10 import _interpolator10


class _nmr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Interpolate_shift = None
        self.Nics = None
        self.Nics_file_name = None
        self.Restart_nmr = None
        self.Shift_gapw_radius = None
        self.PRINT = _print55()
        self.INTERPOLATOR = _interpolator10()
        self._name = "NMR"
        self._keywords = {'Restart_nmr': 'RESTART_NMR', 'Nics': 'NICS', 'Shift_gapw_radius': 'SHIFT_GAPW_RADIUS', 'Interpolate_shift': 'INTERPOLATE_SHIFT', 'Nics_file_name': 'NICS_FILE_NAME'}
        self._subsections = {'PRINT': 'PRINT', 'INTERPOLATOR': 'INTERPOLATOR'}
        self._attributes = ['Section_parameters']

