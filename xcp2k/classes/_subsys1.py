from xcp2k.inputsection import InputSection
from xcp2k.classes._rng_init11 import _rng_init11
from xcp2k.classes._cell4 import _cell4
from xcp2k.classes._coord10 import _coord10
from xcp2k.classes._velocity10 import _velocity10
from xcp2k.classes._kind1 import _kind1
from xcp2k.classes._topology1 import _topology1
from xcp2k.classes._colvar5 import _colvar5
from xcp2k.classes._multipoles4 import _multipoles4
from xcp2k.classes._shell_coord1 import _shell_coord1
from xcp2k.classes._shell_velocity1 import _shell_velocity1
from xcp2k.classes._core_coord1 import _core_coord1
from xcp2k.classes._core_velocity1 import _core_velocity1
from xcp2k.classes._print70 import _print70


class _subsys1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Seed = None
        self.RNG_INIT = _rng_init11()
        self.CELL = _cell4()
        self.COORD = _coord10()
        self.VELOCITY = _velocity10()
        self.KIND_list = []
        self.TOPOLOGY = _topology1()
        self.COLVAR_list = []
        self.MULTIPOLES = _multipoles4()
        self.SHELL_COORD = _shell_coord1()
        self.SHELL_VELOCITY = _shell_velocity1()
        self.CORE_COORD = _core_coord1()
        self.CORE_VELOCITY = _core_velocity1()
        self.PRINT = _print70()
        self._name = "SUBSYS"
        self._keywords = {'Seed': 'SEED'}
        self._subsections = {'RNG_INIT': 'RNG_INIT', 'CELL': 'CELL', 'COORD': 'COORD', 'VELOCITY': 'VELOCITY', 'TOPOLOGY': 'TOPOLOGY', 'MULTIPOLES': 'MULTIPOLES', 'SHELL_COORD': 'SHELL_COORD', 'SHELL_VELOCITY': 'SHELL_VELOCITY', 'CORE_COORD': 'CORE_COORD', 'CORE_VELOCITY': 'CORE_VELOCITY', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'KIND': '_kind1', 'COLVAR': '_colvar5'}
        self._attributes = ['KIND_list', 'COLVAR_list']

    def KIND_add(self, section_parameters=None):
        new_section = _kind1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KIND_list.append(new_section)
        return new_section

    def COLVAR_add(self, section_parameters=None):
        new_section = _colvar5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.COLVAR_list.append(new_section)
        return new_section

