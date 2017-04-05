from xcp2k.inputsection import InputSection
from _ddapc_restraint_a1 import _ddapc_restraint_a1
from _ddapc_restraint_b1 import _ddapc_restraint_b1
from _becke_restraint_a1 import _becke_restraint_a1
from _becke_restraint_b1 import _becke_restraint_b1
from _program_run_info42 import _program_run_info42


class _et_coupling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type_of_constraint = None
        self.DDAPC_RESTRAINT_A = _ddapc_restraint_a1()
        self.DDAPC_RESTRAINT_B = _ddapc_restraint_b1()
        self.BECKE_RESTRAINT_A = _becke_restraint_a1()
        self.BECKE_RESTRAINT_B = _becke_restraint_b1()
        self.PROGRAM_RUN_INFO = _program_run_info42()
        self._name = "ET_COUPLING"
        self._keywords = {'Type_of_constraint': 'TYPE_OF_CONSTRAINT'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'BECKE_RESTRAINT_A': 'BECKE_RESTRAINT_A', 'DDAPC_RESTRAINT_B': 'DDAPC_RESTRAINT_B', 'DDAPC_RESTRAINT_A': 'DDAPC_RESTRAINT_A', 'BECKE_RESTRAINT_B': 'BECKE_RESTRAINT_B'}

