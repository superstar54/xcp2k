from xcp2k.inputsection import InputSection
from _contact1 import _contact1


class _transport1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Transport_method = None
        self.N_abscissae = None
        self.N_kpoints = None
        self.Num_interval = None
        self.Tasks_per_point = None
        self.Colzero_threshold = None
        self.Eps_limit = None
        self.Eps_decay = None
        self.Eps_singularity_curvatures = None
        self.Eps_mu = None
        self.Eps_eigval_degen = None
        self.Energy_interval = None
        self.Min_interval = None
        self.Temperature = None
        self.Row_distribution = None
        self.Csr_screening = None
        self.Linear_solver = None
        self.Injection_method = None
        self.Cutout = None
        self.CONTACT_list = []
        self._name = "TRANSPORT"
        self._keywords = {'Min_interval': 'MIN_INTERVAL', 'Transport_method': 'TRANSPORT_METHOD', 'Linear_solver': 'LINEAR_SOLVER', 'Eps_eigval_degen': 'EPS_EIGVAL_DEGEN', 'Eps_decay': 'EPS_DECAY', 'Eps_mu': 'EPS_MU', 'Eps_limit': 'EPS_LIMIT', 'Colzero_threshold': 'COLZERO_THRESHOLD', 'Energy_interval': 'ENERGY_INTERVAL', 'Num_interval': 'NUM_INTERVAL', 'Row_distribution': 'ROW_DISTRIBUTION', 'Tasks_per_point': 'TASKS_PER_POINT', 'N_abscissae': 'N_ABSCISSAE', 'Injection_method': 'INJECTION_METHOD', 'Eps_singularity_curvatures': 'EPS_SINGULARITY_CURVATURES', 'N_kpoints': 'N_KPOINTS', 'Csr_screening': 'CSR_SCREENING', 'Cutout': 'CUTOUT', 'Temperature': 'TEMPERATURE'}
        self._repeated_subsections = {'CONTACT': '_contact1'}
        self._attributes = ['CONTACT_list']

    def CONTACT_add(self, section_parameters=None):
        new_section = _contact1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONTACT_list.append(new_section)
        return new_section

