from xcp2k.inputsection import InputSection
from xcp2k.classes._print72 import _print72
from xcp2k.classes._interpolator9 import _interpolator9


class _current3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Gauge = None
        self.Gauge_atom_radius = None
        self.Use_old_gauge_atom = None
        self.Orbital_center = None
        self.Common_center = None
        self.Nbox = None
        self.Chi_pbc = None
        self.Force_no_full = None
        self.Selected_states_on_atom_list = []
        self.Selected_states_atom_radius = None
        self.Restart_current = None
        self.PRINT = _print72()
        self.INTERPOLATOR = _interpolator9()
        self._name = "CURRENT"
        self._keywords = {'Gauge': 'GAUGE', 'Gauge_atom_radius': 'GAUGE_ATOM_RADIUS', 'Use_old_gauge_atom': 'USE_OLD_GAUGE_ATOM', 'Orbital_center': 'ORBITAL_CENTER', 'Common_center': 'COMMON_CENTER', 'Nbox': 'NBOX', 'Chi_pbc': 'CHI_PBC', 'Force_no_full': 'FORCE_NO_FULL', 'Selected_states_atom_radius': 'SELECTED_STATES_ATOM_RADIUS', 'Restart_current': 'RESTART_CURRENT'}
        self._repeated_keywords = {'Selected_states_on_atom_list': 'SELECTED_STATES_ON_ATOM_LIST'}
        self._subsections = {'PRINT': 'PRINT', 'INTERPOLATOR': 'INTERPOLATOR'}
        self._attributes = ['Section_parameters']

