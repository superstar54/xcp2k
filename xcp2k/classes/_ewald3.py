from xcp2k.inputsection import InputSection
from _rs_grid5 import _rs_grid5
from _multipoles3 import _multipoles3
from _print37 import _print37


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
        self.PRINT = _print37()
        self._name = "EWALD"
        self._keywords = {'Gmax': 'GMAX', 'Ns_max': 'NS_MAX', 'Epsilon': 'EPSILON', 'O_spline': 'O_SPLINE', 'Rcut': 'RCUT', 'Ewald_accuracy': 'EWALD_ACCURACY', 'Alpha': 'ALPHA', 'Ewald_type': 'EWALD_TYPE'}
        self._subsections = {'PRINT': 'PRINT', 'MULTIPOLES': 'MULTIPOLES'}
        self._repeated_subsections = {'RS_GRID': '_rs_grid5'}
        self._attributes = ['RS_GRID_list']

    def RS_GRID_add(self, section_parameters=None):
        new_section = _rs_grid5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RS_GRID_list.append(new_section)
        return new_section

