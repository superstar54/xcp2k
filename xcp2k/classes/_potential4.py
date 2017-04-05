from xcp2k.inputsection import InputSection
from _gth_potential1 import _gth_potential1


class _potential4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Confinement = None
        self.Pseudo_type = None
        self.Potential_file_name = None
        self.Potential_name = None
        self.GTH_POTENTIAL = _gth_potential1()
        self._name = "POTENTIAL"
        self._keywords = {'Pseudo_type': 'PSEUDO_TYPE', 'Confinement': 'CONFINEMENT', 'Potential_file_name': 'POTENTIAL_FILE_NAME', 'Potential_name': 'POTENTIAL_NAME'}
        self._subsections = {'GTH_POTENTIAL': 'GTH_POTENTIAL'}
        self._aliases = {'Pot_name': 'Potential_name'}


    @property
    def Pot_name(self):
        """
        See documentation for Potential_name
        """
        return self.Potential_name

    @Pot_name.setter
    def Pot_name(self, value):
        self.Potential_name = value
