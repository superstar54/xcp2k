from xcp2k.inputsection import InputSection
from _derivatives2 import _derivatives2
from _ewald_info2 import _ewald_info2
from _dipole3 import _dipole3
from _neighbor_lists6 import _neighbor_lists6
from _iter_info1 import _iter_info1
from _subcell3 import _subcell3
from _program_banner2 import _program_banner2
from _program_run_info30 import _program_run_info30
from _ff_parameter_file1 import _ff_parameter_file1
from _ff_info1 import _ff_info1


class _print44(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DERIVATIVES = _derivatives2()
        self.EWALD_INFO = _ewald_info2()
        self.DIPOLE = _dipole3()
        self.NEIGHBOR_LISTS = _neighbor_lists6()
        self.ITER_INFO = _iter_info1()
        self.SUBCELL = _subcell3()
        self.PROGRAM_BANNER = _program_banner2()
        self.PROGRAM_RUN_INFO = _program_run_info30()
        self.FF_PARAMETER_FILE = _ff_parameter_file1()
        self.FF_INFO = _ff_info1()
        self._name = "PRINT"
        self._subsections = {'DERIVATIVES': 'DERIVATIVES', 'EWALD_INFO': 'EWALD_INFO', 'ITER_INFO': 'ITER_INFO', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'SUBCELL': 'SUBCELL', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'FF_INFO': 'FF_INFO', 'DIPOLE': 'DIPOLE', 'FF_PARAMETER_FILE': 'FF_PARAMETER_FILE', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS'}

