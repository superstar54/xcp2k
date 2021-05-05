from xcp2k.inputsection import InputSection
from xcp2k.classes._ri_metric3 import _ri_metric3
from xcp2k.classes._opt_ri_basis3 import _opt_ri_basis3


class _ri9(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Row_block = None
        self.Col_block = None
        self.Calc_cond_num = None
        self.Do_svd = None
        self.Eps_svd = None
        self.Eri_blksize = None
        self.RI_METRIC = _ri_metric3()
        self.OPT_RI_BASIS = _opt_ri_basis3()
        self._name = "RI"
        self._keywords = {'Row_block': 'ROW_BLOCK', 'Col_block': 'COL_BLOCK', 'Calc_cond_num': 'CALC_COND_NUM', 'Do_svd': 'DO_SVD', 'Eps_svd': 'EPS_SVD', 'Eri_blksize': 'ERI_BLKSIZE'}
        self._subsections = {'RI_METRIC': 'RI_METRIC', 'OPT_RI_BASIS': 'OPT_RI_BASIS'}
        self._aliases = {'Row_block_size': 'Row_block', 'Col_block_size': 'Col_block', 'Calc_condition_number': 'Calc_cond_num'}


    @property
    def Row_block_size(self):
        """
        See documentation for Row_block
        """
        return self.Row_block

    @property
    def Col_block_size(self):
        """
        See documentation for Col_block
        """
        return self.Col_block

    @property
    def Calc_condition_number(self):
        """
        See documentation for Calc_cond_num
        """
        return self.Calc_cond_num

    @Row_block_size.setter
    def Row_block_size(self, value):
        self.Row_block = value

    @Col_block_size.setter
    def Col_block_size(self, value):
        self.Col_block = value

    @Calc_condition_number.setter
    def Calc_condition_number(self, value):
        self.Calc_cond_num = value
