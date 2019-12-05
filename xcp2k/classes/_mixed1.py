from xcp2k.inputsection import InputSection
from xcp2k.classes._linear1 import _linear1
from xcp2k.classes._mixed_cdft1 import _mixed_cdft1
from xcp2k.classes._coupling1 import _coupling1
from xcp2k.classes._restraint7 import _restraint7
from xcp2k.classes._generic1 import _generic1
from xcp2k.classes._mapping1 import _mapping1
from xcp2k.classes._print18 import _print18


class _mixed1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mixing_type = None
        self.Group_partition = None
        self.Ngroups = None
        self.LINEAR = _linear1()
        self.MIXED_CDFT = _mixed_cdft1()
        self.COUPLING = _coupling1()
        self.RESTRAINT = _restraint7()
        self.GENERIC = _generic1()
        self.MAPPING_list = []
        self.PRINT = _print18()
        self._name = "MIXED"
        self._keywords = {'Mixing_type': 'MIXING_TYPE', 'Group_partition': 'GROUP_PARTITION', 'Ngroups': 'NGROUPS'}
        self._subsections = {'LINEAR': 'LINEAR', 'MIXED_CDFT': 'MIXED_CDFT', 'COUPLING': 'COUPLING', 'RESTRAINT': 'RESTRAINT', 'GENERIC': 'GENERIC', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'MAPPING': '_mapping1'}
        self._aliases = {'Ngroup': 'Ngroups'}
        self._attributes = ['MAPPING_list']

    def MAPPING_add(self, section_parameters=None):
        new_section = _mapping1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MAPPING_list.append(new_section)
        return new_section


    @property
    def Ngroup(self):
        """
        See documentation for Ngroups
        """
        return self.Ngroups

    @Ngroup.setter
    def Ngroup(self, value):
        self.Ngroups = value
