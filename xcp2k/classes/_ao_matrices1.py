from xcp2k.inputsection import InputSection
from xcp2k.classes._each341 import _each341


class _ao_matrices1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Omit_headers = None
        self.Ndigits = None
        self.Core_hamiltonian = None
        self.Density = None
        self.Kinetic_energy = None
        self.Kohn_sham_matrix = None
        self.Matrix_vxc = None
        self.Ortho = None
        self.Overlap = None
        self.Commutator_hr = None
        self.Fermi_contact = None
        self.Pso = None
        self.Efg = None
        self.Potential_energy = None
        self.Oce_hard = None
        self.Oce_soft = None
        self.W_matrix = None
        self.W_matrix_aux_fit = None
        self.Derivatives = None
        self.EACH = _each341()
        self._name = "AO_MATRICES"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Omit_headers': 'OMIT_HEADERS', 'Ndigits': 'NDIGITS', 'Core_hamiltonian': 'CORE_HAMILTONIAN', 'Density': 'DENSITY', 'Kinetic_energy': 'KINETIC_ENERGY', 'Kohn_sham_matrix': 'KOHN_SHAM_MATRIX', 'Matrix_vxc': 'MATRIX_VXC', 'Ortho': 'ORTHO', 'Overlap': 'OVERLAP', 'Commutator_hr': 'COMMUTATOR_HR', 'Fermi_contact': 'FERMI_CONTACT', 'Pso': 'PSO', 'Efg': 'EFG', 'Potential_energy': 'POTENTIAL_ENERGY', 'Oce_hard': 'OCE_HARD', 'Oce_soft': 'OCE_SOFT', 'W_matrix': 'W_MATRIX', 'W_matrix_aux_fit': 'W_MATRIX_AUX_FIT', 'Derivatives': 'DERIVATIVES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

