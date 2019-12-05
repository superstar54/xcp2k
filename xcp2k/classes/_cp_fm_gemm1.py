from xcp2k.inputsection import InputSection


class _cp_fm_gemm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_loop = None
        self.K = None
        self.M = None
        self.N = None
        self.Nrow_block = None
        self.Ncol_block = None
        self.Row_major = None
        self.Force_blocksize = None
        self.Grid_2d = None
        self.Transa = None
        self.Transb = None
        self._name = "CP_FM_GEMM"
        self._keywords = {'N_loop': 'N_LOOP', 'K': 'K', 'M': 'M', 'N': 'N', 'Nrow_block': 'NROW_BLOCK', 'Ncol_block': 'NCOL_BLOCK', 'Row_major': 'ROW_MAJOR', 'Force_blocksize': 'FORCE_BLOCKSIZE', 'Grid_2d': 'GRID_2D', 'Transa': 'TRANSA', 'Transb': 'TRANSB'}

