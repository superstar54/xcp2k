from xcp2k.inputsection import InputSection


class _davidson3(InputSection):
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
        self._keywords = {'Preconditioner': 'PRECONDITIONER', 'Precond_solver': 'PRECOND_SOLVER', 'Energy_gap': 'ENERGY_GAP', 'New_prec_each': 'NEW_PREC_EACH', 'First_prec': 'FIRST_PREC', 'Conv_mos_percent': 'CONV_MOS_PERCENT', 'Sparse_mos': 'SPARSE_MOS'}

