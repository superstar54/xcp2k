from xcp2k.inputsection import InputSection
from xcp2k.classes._contact1 import _contact1
from xcp2k.classes._beyn1 import _beyn1
from xcp2k.classes._pexsi2 import _pexsi2
from xcp2k.classes._print46 import _print46


class _transport1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Transport_method = None
        self.Qt_formalism = None
        self.Num_pole = None
        self.N_kpoints = None
        self.Num_interval = None
        self.Tasks_per_energy_point = None
        self.Tasks_per_pole = None
        self.Gpus_per_point = None
        self.Colzero_threshold = None
        self.Eps_limit = None
        self.Eps_limit_cc = None
        self.Eps_decay = None
        self.Eps_singularity_curvatures = None
        self.Eps_mu = None
        self.Eps_eigval_degen = None
        self.Eps_fermi = None
        self.Energy_interval = None
        self.Min_interval = None
        self.Temperature = None
        self.Csr_screening = None
        self.Linear_solver = None
        self.Matrix_inversion_method = None
        self.Injection_method = None
        self.Cutout = None
        self.Real_axis_integration_method = None
        self.N_points_inv = None
        self.Obc_equilibrium = None
        self.Contact_filling = None
        self.Density_mixing = None
        self.CONTACT_list = []
        self.BEYN = _beyn1()
        self.PEXSI = _pexsi2()
        self.PRINT = _print46()
        self._name = "TRANSPORT"
        self._keywords = {'Transport_method': 'TRANSPORT_METHOD', 'Qt_formalism': 'QT_FORMALISM', 'Num_pole': 'NUM_POLE', 'N_kpoints': 'N_KPOINTS', 'Num_interval': 'NUM_INTERVAL', 'Tasks_per_energy_point': 'TASKS_PER_ENERGY_POINT', 'Tasks_per_pole': 'TASKS_PER_POLE', 'Gpus_per_point': 'GPUS_PER_POINT', 'Colzero_threshold': 'COLZERO_THRESHOLD', 'Eps_limit': 'EPS_LIMIT', 'Eps_limit_cc': 'EPS_LIMIT_CC', 'Eps_decay': 'EPS_DECAY', 'Eps_singularity_curvatures': 'EPS_SINGULARITY_CURVATURES', 'Eps_mu': 'EPS_MU', 'Eps_eigval_degen': 'EPS_EIGVAL_DEGEN', 'Eps_fermi': 'EPS_FERMI', 'Energy_interval': 'ENERGY_INTERVAL', 'Min_interval': 'MIN_INTERVAL', 'Temperature': 'TEMPERATURE', 'Csr_screening': 'CSR_SCREENING', 'Linear_solver': 'LINEAR_SOLVER', 'Matrix_inversion_method': 'MATRIX_INVERSION_METHOD', 'Injection_method': 'INJECTION_METHOD', 'Cutout': 'CUTOUT', 'Real_axis_integration_method': 'REAL_AXIS_INTEGRATION_METHOD', 'N_points_inv': 'N_POINTS_INV', 'Obc_equilibrium': 'OBC_EQUILIBRIUM', 'Contact_filling': 'CONTACT_FILLING', 'Density_mixing': 'DENSITY_MIXING'}
        self._subsections = {'BEYN': 'BEYN', 'PEXSI': 'PEXSI', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'CONTACT': '_contact1'}
        self._attributes = ['CONTACT_list']

    def CONTACT_add(self, section_parameters=None):
        new_section = _contact1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONTACT_list.append(new_section)
        return new_section

