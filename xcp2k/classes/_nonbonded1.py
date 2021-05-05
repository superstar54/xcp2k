from xcp2k.inputsection import InputSection
from xcp2k.classes._genpot1 import _genpot1


class _nonbonded1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dx = None
        self.Error_limit = None
        self.GENPOT_list = []
        self._name = "NONBONDED"
        self._keywords = {'Dx': 'DX', 'Error_limit': 'ERROR_LIMIT'}
        self._repeated_subsections = {'GENPOT': '_genpot1'}
        self._attributes = ['GENPOT_list']

    def GENPOT_add(self, section_parameters=None):
        new_section = _genpot1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GENPOT_list.append(new_section)
        return new_section

