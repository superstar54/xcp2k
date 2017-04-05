from xcp2k.inputsection import InputSection
from _point65 import _point65


class _qparm4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_from = []
        self.Points_from = self.Atoms_from
        self.Atoms_to = []
        self.Points_to = self.Atoms_to
        self.Rcut = None
        self.L = None
        self.Alpha = None
        self.POINT_list = []
        self._name = "QPARM"
        self._keywords = {'Alpha': 'ALPHA', 'L': 'L', 'Rcut': 'RCUT'}
        self._repeated_keywords = {'Atoms_to': 'ATOMS_TO', 'Atoms_from': 'ATOMS_FROM'}
        self._repeated_subsections = {'POINT': '_point65'}
        self._repeated_aliases = {'Points_to': 'Atoms_to', 'Points_from': 'Atoms_from'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point65()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

