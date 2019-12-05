from xcp2k.inputsection import InputSection


class _fm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nrow_blocks = None
        self.Ncol_blocks = None
        self.Force_block_size = None
        self.Type_of_matrix_multiplication = None
        self._name = "FM"
        self._keywords = {'Nrow_blocks': 'NROW_BLOCKS', 'Ncol_blocks': 'NCOL_BLOCKS', 'Force_block_size': 'FORCE_BLOCK_SIZE', 'Type_of_matrix_multiplication': 'TYPE_OF_MATRIX_MULTIPLICATION'}

