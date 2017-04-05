from xcp2k.inputsection import InputSection
from _localize3 import _localize3
from _current2 import _current2
from _nmr1 import _nmr1
from _spinspin1 import _spinspin1
from _epr1 import _epr1
from _polar1 import _polar1
from _print55 import _print55


class _linres1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps = None
        self.Max_iter = None
        self.Restart_every = None
        self.Preconditioner = None
        self.Energy_gap = None
        self.Restart = None
        self.Wfn_restart_file_name = None
        self.LOCALIZE = _localize3()
        self.CURRENT = _current2()
        self.NMR = _nmr1()
        self.SPINSPIN = _spinspin1()
        self.EPR = _epr1()
        self.POLAR = _polar1()
        self.PRINT = _print55()
        self._name = "LINRES"
        self._keywords = {'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME', 'Max_iter': 'MAX_ITER', 'Eps': 'EPS', 'Preconditioner': 'PRECONDITIONER', 'Energy_gap': 'ENERGY_GAP', 'Restart_every': 'RESTART_EVERY', 'Restart': 'RESTART'}
        self._subsections = {'POLAR': 'POLAR', 'NMR': 'NMR', 'EPR': 'EPR', 'CURRENT': 'CURRENT', 'PRINT': 'PRINT', 'SPINSPIN': 'SPINSPIN', 'LOCALIZE': 'LOCALIZE'}
        self._aliases = {'Restart_file_name': 'Wfn_restart_file_name'}


    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
