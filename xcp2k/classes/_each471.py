from xcp2k.inputsection import InputSection


class _each471(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Just_energy = None
        self.Powell_opt = None
        self.Qs_scf = None
        self.Xas_scf = None
        self.Md = None
        self.Pint = None
        self.Metadynamics = None
        self.Geo_opt = None
        self.Rot_opt = None
        self.Cell_opt = None
        self.Band = None
        self.Ep_lin_solver = None
        self.Spline_find_coeffs = None
        self.Replica_eval = None
        self.Bsse = None
        self.Shell_opt = None
        self.Tddft_scf = None
        self._name = "EACH"
        self._keywords = {'Just_energy': 'JUST_ENERGY', 'Powell_opt': 'POWELL_OPT', 'Qs_scf': 'QS_SCF', 'Xas_scf': 'XAS_SCF', 'Md': 'MD', 'Pint': 'PINT', 'Metadynamics': 'METADYNAMICS', 'Geo_opt': 'GEO_OPT', 'Rot_opt': 'ROT_OPT', 'Cell_opt': 'CELL_OPT', 'Band': 'BAND', 'Ep_lin_solver': 'EP_LIN_SOLVER', 'Spline_find_coeffs': 'SPLINE_FIND_COEFFS', 'Replica_eval': 'REPLICA_EVAL', 'Bsse': 'BSSE', 'Shell_opt': 'SHELL_OPT', 'Tddft_scf': 'TDDFT_SCF'}

