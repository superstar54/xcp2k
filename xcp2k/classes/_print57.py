from xcp2k.inputsection import InputSection
from xcp2k.classes._derivatives2 import _derivatives2
from xcp2k.classes._ewald_info2 import _ewald_info2
from xcp2k.classes._dipole3 import _dipole3
from xcp2k.classes._neighbor_lists6 import _neighbor_lists6
from xcp2k.classes._iter_info1 import _iter_info1
from xcp2k.classes._subcell3 import _subcell3
from xcp2k.classes._program_banner2 import _program_banner2
from xcp2k.classes._program_run_info37 import _program_run_info37
from xcp2k.classes._ff_parameter_file1 import _ff_parameter_file1
from xcp2k.classes._ff_info1 import _ff_info1


class _print57(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DERIVATIVES = _derivatives2()
        self.EWALD_INFO = _ewald_info2()
        self.DIPOLE = _dipole3()
        self.NEIGHBOR_LISTS = _neighbor_lists6()
        self.ITER_INFO = _iter_info1()
        self.SUBCELL = _subcell3()
        self.PROGRAM_BANNER = _program_banner2()
        self.PROGRAM_RUN_INFO = _program_run_info37()
        self.FF_PARAMETER_FILE = _ff_parameter_file1()
        self.FF_INFO = _ff_info1()
        self._name = "PRINT"
        self._subsections = {'DERIVATIVES': 'DERIVATIVES', 'EWALD_INFO': 'EWALD_INFO', 'DIPOLE': 'DIPOLE', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'ITER_INFO': 'ITER_INFO', 'SUBCELL': 'SUBCELL', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'FF_PARAMETER_FILE': 'FF_PARAMETER_FILE', 'FF_INFO': 'FF_INFO'}

