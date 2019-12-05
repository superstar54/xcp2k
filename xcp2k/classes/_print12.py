from xcp2k.inputsection import InputSection
from xcp2k.classes._energy5 import _energy5
from xcp2k.classes._shell_energy1 import _shell_energy1
from xcp2k.classes._temp_kind1 import _temp_kind1
from xcp2k.classes._temp_shell_kind1 import _temp_shell_kind1
from xcp2k.classes._center_of_mass1 import _center_of_mass1
from xcp2k.classes._coefficients1 import _coefficients1
from xcp2k.classes._rotational_info2 import _rotational_info2
from xcp2k.classes._program_run_info8 import _program_run_info8


class _print12(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Force_last = None
        self.ENERGY = _energy5()
        self.SHELL_ENERGY = _shell_energy1()
        self.TEMP_KIND = _temp_kind1()
        self.TEMP_SHELL_KIND = _temp_shell_kind1()
        self.CENTER_OF_MASS = _center_of_mass1()
        self.COEFFICIENTS = _coefficients1()
        self.ROTATIONAL_INFO = _rotational_info2()
        self.PROGRAM_RUN_INFO = _program_run_info8()
        self._name = "PRINT"
        self._keywords = {'Force_last': 'FORCE_LAST'}
        self._subsections = {'ENERGY': 'ENERGY', 'SHELL_ENERGY': 'SHELL_ENERGY', 'TEMP_KIND': 'TEMP_KIND', 'TEMP_SHELL_KIND': 'TEMP_SHELL_KIND', 'CENTER_OF_MASS': 'CENTER_OF_MASS', 'COEFFICIENTS': 'COEFFICIENTS', 'ROTATIONAL_INFO': 'ROTATIONAL_INFO', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

