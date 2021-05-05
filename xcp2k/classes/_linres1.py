from xcp2k.inputsection import InputSection
from xcp2k.classes._localize12 import _localize12
from xcp2k.classes._current3 import _current3
from xcp2k.classes._nmr1 import _nmr1
from xcp2k.classes._spinspin1 import _spinspin1
from xcp2k.classes._epr1 import _epr1
from xcp2k.classes._polar1 import _polar1
from xcp2k.classes._print82 import _print82


class _linres1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps = None
        self.Eps_filter = None
        self.Max_iter = None
        self.Restart_every = None
        self.Preconditioner = None
        self.Energy_gap = None
        self.Restart = None
        self.Wfn_restart_file_name = None
        self.LOCALIZE = _localize12()
        self.CURRENT = _current3()
        self.NMR = _nmr1()
        self.SPINSPIN = _spinspin1()
        self.EPR = _epr1()
        self.POLAR = _polar1()
        self.PRINT = _print82()
        self._name = "LINRES"
        self._keywords = {'Eps': 'EPS', 'Eps_filter': 'EPS_FILTER', 'Max_iter': 'MAX_ITER', 'Restart_every': 'RESTART_EVERY', 'Preconditioner': 'PRECONDITIONER', 'Energy_gap': 'ENERGY_GAP', 'Restart': 'RESTART', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME'}
        self._subsections = {'LOCALIZE': 'LOCALIZE', 'CURRENT': 'CURRENT', 'NMR': 'NMR', 'SPINSPIN': 'SPINSPIN', 'EPR': 'EPR', 'POLAR': 'POLAR', 'PRINT': 'PRINT'}
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
