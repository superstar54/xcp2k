from xcp2k.inputsection import InputSection
from _restart15 import _restart15


class _zmp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_density = None
        self.Grid_tol = None
        self.Lambda = None
        self.Dm = None
        self.RESTART = _restart15()
        self._name = "ZMP"
        self._keywords = {'Grid_tol': 'GRID_TOL', 'File_density': 'FILE_DENSITY', 'Dm': 'DM', 'Lambda': 'LAMBDA'}
        self._subsections = {'RESTART': 'RESTART'}

