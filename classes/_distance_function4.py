from xcp2k.inputsection import InputSection
from _point64 import _point64


class _distance_function4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Coefficient = None
        self.Pbc = None
        self.POINT_list = []
        self._name = "DISTANCE_FUNCTION"
        self._keywords = {'Coefficient': 'COEFFICIENT', 'Pbc': 'PBC', 'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point64'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point64()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def Points(self):
        """
        See documentation for Atoms
        """
        return self.Atoms

    @Points.setter
    def Points(self, value):
        self.Atoms = value
