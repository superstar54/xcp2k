from xcp2k.inputsection import InputSection
from xcp2k.classes._forcefield1 import _forcefield1
from xcp2k.classes._neighbor_lists5 import _neighbor_lists5
from xcp2k.classes._poisson2 import _poisson2
from xcp2k.classes._periodic_efield2 import _periodic_efield2
from xcp2k.classes._print57 import _print57


class _mm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.FORCEFIELD = _forcefield1()
        self.NEIGHBOR_LISTS = _neighbor_lists5()
        self.POISSON = _poisson2()
        self.PERIODIC_EFIELD_list = []
        self.PRINT = _print57()
        self._name = "MM"
        self._subsections = {'FORCEFIELD': 'FORCEFIELD', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'POISSON': 'POISSON', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'PERIODIC_EFIELD': '_periodic_efield2'}
        self._attributes = ['PERIODIC_EFIELD_list']

    def PERIODIC_EFIELD_add(self, section_parameters=None):
        new_section = _periodic_efield2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PERIODIC_EFIELD_list.append(new_section)
        return new_section

