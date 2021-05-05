from xcp2k.inputsection import InputSection
from xcp2k.classes._contact2 import _contact2
from xcp2k.classes._scattering_region1 import _scattering_region1
from xcp2k.classes._mixing5 import _mixing5
from xcp2k.classes._print97 import _print97


class _negf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Disable_cache = None
        self.Eps_density = None
        self.Eps_green = None
        self.Eps_scf = None
        self.Eps_geo = None
        self.Energy_lbound = None
        self.Eta = None
        self.Homo_lumo_gap = None
        self.Delta_npoles = None
        self.Gamma_kt = None
        self.Integration_method = None
        self.Integration_min_points = None
        self.Integration_max_points = None
        self.Max_scf = None
        self.Nproc_point = None
        self.V_shift = None
        self.V_shift_offset = None
        self.V_shift_max_iters = None
        self.CONTACT_list = []
        self.SCATTERING_REGION = _scattering_region1()
        self.MIXING = _mixing5()
        self.PRINT = _print97()
        self._name = "NEGF"
        self._keywords = {'Disable_cache': 'DISABLE_CACHE', 'Eps_density': 'EPS_DENSITY', 'Eps_green': 'EPS_GREEN', 'Eps_scf': 'EPS_SCF', 'Eps_geo': 'EPS_GEO', 'Energy_lbound': 'ENERGY_LBOUND', 'Eta': 'ETA', 'Homo_lumo_gap': 'HOMO_LUMO_GAP', 'Delta_npoles': 'DELTA_NPOLES', 'Gamma_kt': 'GAMMA_KT', 'Integration_method': 'INTEGRATION_METHOD', 'Integration_min_points': 'INTEGRATION_MIN_POINTS', 'Integration_max_points': 'INTEGRATION_MAX_POINTS', 'Max_scf': 'MAX_SCF', 'Nproc_point': 'NPROC_POINT', 'V_shift': 'V_SHIFT', 'V_shift_offset': 'V_SHIFT_OFFSET', 'V_shift_max_iters': 'V_SHIFT_MAX_ITERS'}
        self._subsections = {'SCATTERING_REGION': 'SCATTERING_REGION', 'MIXING': 'MIXING', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'CONTACT': '_contact2'}
        self._attributes = ['CONTACT_list']

    def CONTACT_add(self, section_parameters=None):
        new_section = _contact2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONTACT_list.append(new_section)
        return new_section

