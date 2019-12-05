from xcp2k.inputsection import InputSection
from xcp2k.classes._dielectric_cube1 import _dielectric_cube1
from xcp2k.classes._dirichlet_bc_cube1 import _dirichlet_bc_cube1
from xcp2k.classes._dirichlet_cstr_charge_cube1 import _dirichlet_cstr_charge_cube1


class _implicit_psolver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DIELECTRIC_CUBE = _dielectric_cube1()
        self.DIRICHLET_BC_CUBE = _dirichlet_bc_cube1()
        self.DIRICHLET_CSTR_CHARGE_CUBE = _dirichlet_cstr_charge_cube1()
        self._name = "IMPLICIT_PSOLVER"
        self._subsections = {'DIELECTRIC_CUBE': 'DIELECTRIC_CUBE', 'DIRICHLET_BC_CUBE': 'DIRICHLET_BC_CUBE', 'DIRICHLET_CSTR_CHARGE_CUBE': 'DIRICHLET_CSTR_CHARGE_CUBE'}

