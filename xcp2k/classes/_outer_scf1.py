from xcp2k.inputsection import InputSection


class _outer_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Type = None
        self.Optimizer = None
        self.Broyden_type = None
        self.Jacobian_type = None
        self.Jacobian_step = None
        self.Jacobian_freq = None
        self.Jacobian_restart = None
        self.Jacobian_vector = None
        self.Bisect_trust_count = None
        self.Eps_scf = None
        self.Diis_buffer_length = None
        self.Extrapolation_order = None
        self.Max_scf = None
        self.Max_ls = None
        self.Factor_ls = None
        self.Continue_ls = None
        self.Step_size = None
        self._name = "OUTER_SCF"
        self._keywords = {'Max_scf': 'MAX_SCF', 'Jacobian_restart': 'JACOBIAN_RESTART', 'Optimizer': 'OPTIMIZER', 'Jacobian_freq': 'JACOBIAN_FREQ', 'Continue_ls': 'CONTINUE_LS', 'Diis_buffer_length': 'DIIS_BUFFER_LENGTH', 'Factor_ls': 'FACTOR_LS', 'Jacobian_vector': 'JACOBIAN_VECTOR', 'Jacobian_step': 'JACOBIAN_STEP', 'Step_size': 'STEP_SIZE', 'Broyden_type': 'BROYDEN_TYPE', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Eps_scf': 'EPS_SCF', 'Bisect_trust_count': 'BISECT_TRUST_COUNT', 'Type': 'TYPE', 'Max_ls': 'MAX_LS', 'Jacobian_type': 'JACOBIAN_TYPE'}
        self._attributes = ['Section_parameters']

