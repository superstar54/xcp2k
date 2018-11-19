from xcp2k.inputsection import InputSection
from _mo_cubes2 import _mo_cubes2


class _print65(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mo_coeff_atom = []
        self.Mo_coeff_atom_state = []
        self.MO_CUBES = _mo_cubes2()
        self._name = "PRINT"
        self._repeated_keywords = {'Mo_coeff_atom_state': 'MO_COEFF_ATOM_STATE', 'Mo_coeff_atom': 'MO_COEFF_ATOM'}
        self._subsections = {'MO_CUBES': 'MO_CUBES'}

