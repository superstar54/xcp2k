from xcp2k.inputsection import InputSection
from xcp2k.classes._point32 import _point32


class _hbp2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Shift = None
        self.Npoints = None
        self.Atoms = []
        self.Points = self.Atoms
        self.POINT_list = []
        self._name = "HBP"
        self._keywords = {'Rcut': 'RCUT', 'Shift': 'SHIFT', 'Npoints': 'NPOINTS'}
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point32'}
        self._repeated_aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point32()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

