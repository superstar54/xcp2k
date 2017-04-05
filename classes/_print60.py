from xcp2k.inputsection import InputSection
from _banner2 import _banner2
from _program_run_info46 import _program_run_info46
from _molden_vib1 import _molden_vib1
from _rotational_info3 import _rotational_info3


class _print60(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.BANNER = _banner2()
        self.PROGRAM_RUN_INFO = _program_run_info46()
        self.MOLDEN_VIB = _molden_vib1()
        self.ROTATIONAL_INFO = _rotational_info3()
        self._name = "PRINT"
        self._subsections = {'ROTATIONAL_INFO': 'ROTATIONAL_INFO', 'BANNER': 'BANNER', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'MOLDEN_VIB': 'MOLDEN_VIB'}

