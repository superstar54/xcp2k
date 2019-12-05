from xcp2k.inputsection import InputSection
from xcp2k.classes._banner2 import _banner2
from xcp2k.classes._program_run_info51 import _program_run_info51
from xcp2k.classes._molden_vib1 import _molden_vib1
from xcp2k.classes._rotational_info3 import _rotational_info3
from xcp2k.classes._cartesian_eigs1 import _cartesian_eigs1
from xcp2k.classes._hessian1 import _hessian1


class _print71(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.BANNER = _banner2()
        self.PROGRAM_RUN_INFO = _program_run_info51()
        self.MOLDEN_VIB = _molden_vib1()
        self.ROTATIONAL_INFO = _rotational_info3()
        self.CARTESIAN_EIGS = _cartesian_eigs1()
        self.HESSIAN = _hessian1()
        self._name = "PRINT"
        self._subsections = {'BANNER': 'BANNER', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'MOLDEN_VIB': 'MOLDEN_VIB', 'ROTATIONAL_INFO': 'ROTATIONAL_INFO', 'CARTESIAN_EIGS': 'CARTESIAN_EIGS', 'HESSIAN': 'HESSIAN'}

