from xcp2k.inputsection import InputSection
from xcp2k.classes._point28 import _point28


class _qparm2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_from = []
        self.Points_from = self.Atoms_from
        self.Atoms_to = []
        self.Points_to = self.Atoms_to
        self.Rcut = None
        self.Include_images = None
        self.Rstart = None
        self.L = None
        self.POINT_list = []
        self._name = "QPARM"
        self._keywords = {'Rcut': 'RCUT', 'Include_images': 'INCLUDE_IMAGES', 'Rstart': 'RSTART', 'L': 'L'}
        self._repeated_keywords = {'Atoms_from': 'ATOMS_FROM', 'Atoms_to': 'ATOMS_TO'}
        self._repeated_subsections = {'POINT': '_point28'}
        self._repeated_aliases = {'Points_from': 'Atoms_from', 'Points_to': 'Atoms_to'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point28()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

