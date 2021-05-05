from xcp2k.inputsection import InputSection
from xcp2k.classes._mapping2 import _mapping2
from xcp2k.classes._print19 import _print19


class _embed1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Embed_method = None
        self.Group_partition = None
        self.Ngroups = None
        self.MAPPING_list = []
        self.PRINT = _print19()
        self._name = "EMBED"
        self._keywords = {'Embed_method': 'EMBED_METHOD', 'Group_partition': 'GROUP_PARTITION', 'Ngroups': 'NGROUPS'}
        self._subsections = {'PRINT': 'PRINT'}
        self._repeated_subsections = {'MAPPING': '_mapping2'}
        self._aliases = {'Ngroup': 'Ngroups'}
        self._attributes = ['MAPPING_list']

    def MAPPING_add(self, section_parameters=None):
        new_section = _mapping2()
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
