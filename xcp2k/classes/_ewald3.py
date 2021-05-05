from xcp2k.inputsection import InputSection
from xcp2k.classes._rs_grid5 import _rs_grid5
from xcp2k.classes._multipoles3 import _multipoles3
from xcp2k.classes._print61 import _print61


class _ewald3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ewald_type = None
        self.Ewald_accuracy = None
        self.Rcut = None
        self.Alpha = None
        self.Gmax = None
        self.Ns_max = None
        self.O_spline = None
        self.Epsilon = None
        self.RS_GRID_list = []
        self.MULTIPOLES = _multipoles3()
        self.PRINT = _print61()
        self._name = "EWALD"
        self._keywords = {'Ewald_type': 'EWALD_TYPE', 'Ewald_accuracy': 'EWALD_ACCURACY', 'Rcut': 'RCUT', 'Alpha': 'ALPHA', 'Gmax': 'GMAX', 'Ns_max': 'NS_MAX', 'O_spline': 'O_SPLINE', 'Epsilon': 'EPSILON'}
        self._subsections = {'MULTIPOLES': 'MULTIPOLES', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'RS_GRID': '_rs_grid5'}
        self._attributes = ['RS_GRID_list']

    def RS_GRID_add(self, section_parameters=None):
        new_section = _rs_grid5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RS_GRID_list.append(new_section)
        return new_section

