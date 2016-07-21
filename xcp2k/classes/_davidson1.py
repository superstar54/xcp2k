from xcp2k.inputsection import InputSection


class _davidson1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Preconditioner = None
        self.Precond_solver = None
        self.Energy_gap = None
        self.New_prec_each = None
        self.First_prec = None
        self.Conv_mos_percent = None
        self.Sparse_mos = None
        self._name = "DAVIDSON"
        self._keywords = {'Precond_solver': 'PRECOND_SOLVER', 'Preconditioner': 'PRECONDITIONER', 'Conv_mos_percent': 'CONV_MOS_PERCENT', 'Energy_gap': 'ENERGY_GAP', 'New_prec_each': 'NEW_PREC_EACH', 'First_prec': 'FIRST_PREC', 'Sparse_mos': 'SPARSE_MOS'}

