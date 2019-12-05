from xcp2k.inputsection import InputSection
from xcp2k.classes._geo_opt1 import _geo_opt1
from xcp2k.classes._cell_opt1 import _cell_opt1
from xcp2k.classes._shell_opt1 import _shell_opt1
from xcp2k.classes._md1 import _md1
from xcp2k.classes._driver1 import _driver1
from xcp2k.classes._free_energy1 import _free_energy1
from xcp2k.classes._constraint1 import _constraint1
from xcp2k.classes._flexible_partitioning1 import _flexible_partitioning1
from xcp2k.classes._mc1 import _mc1
from xcp2k.classes._tmc1 import _tmc1
from xcp2k.classes._pint1 import _pint1
from xcp2k.classes._band1 import _band1
from xcp2k.classes._print16 import _print16


class _motion1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.GEO_OPT = _geo_opt1()
        self.CELL_OPT = _cell_opt1()
        self.SHELL_OPT = _shell_opt1()
        self.MD = _md1()
        self.DRIVER = _driver1()
        self.FREE_ENERGY = _free_energy1()
        self.CONSTRAINT = _constraint1()
        self.FLEXIBLE_PARTITIONING = _flexible_partitioning1()
        self.MC = _mc1()
        self.TMC = _tmc1()
        self.PINT = _pint1()
        self.BAND = _band1()
        self.PRINT_list = []
        self._name = "MOTION"
        self._subsections = {'GEO_OPT': 'GEO_OPT', 'CELL_OPT': 'CELL_OPT', 'SHELL_OPT': 'SHELL_OPT', 'MD': 'MD', 'DRIVER': 'DRIVER', 'FREE_ENERGY': 'FREE_ENERGY', 'CONSTRAINT': 'CONSTRAINT', 'FLEXIBLE_PARTITIONING': 'FLEXIBLE_PARTITIONING', 'MC': 'MC', 'TMC': 'TMC', 'PINT': 'PINT', 'BAND': 'BAND'}
        self._repeated_subsections = {'PRINT': '_print16'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print16()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

