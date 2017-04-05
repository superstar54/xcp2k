from xcp2k.inputsection import InputSection
from _mp2_info3 import _mp2_info3
from _direct_canonical3 import _direct_canonical3
from _wfc_gpw3 import _wfc_gpw3
from _ri_mp23 import _ri_mp23
from _opt_ri_basis3 import _opt_ri_basis3
from _ri_rpa3 import _ri_rpa3
from _ri_laplace3 import _ri_laplace3
from _cphf3 import _cphf3
from _interaction_potential9 import _interaction_potential9


class _wf_correlation3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Memory = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.Row_block = None
        self.Col_block = None
        self.Calc_cond_num = None
        self.MP2_INFO = _mp2_info3()
        self.DIRECT_CANONICAL = _direct_canonical3()
        self.WFC_GPW = _wfc_gpw3()
        self.RI_MP2 = _ri_mp23()
        self.OPT_RI_BASIS = _opt_ri_basis3()
        self.RI_RPA = _ri_rpa3()
        self.RI_LAPLACE = _ri_laplace3()
        self.CPHF = _cphf3()
        self.INTERACTION_POTENTIAL = _interaction_potential9()
        self._name = "WF_CORRELATION"
        self._keywords = {'Group_size': 'GROUP_SIZE', 'Row_block': 'ROW_BLOCK', 'Calc_cond_num': 'CALC_COND_NUM', 'Scale_s': 'SCALE_S', 'Scale_t': 'SCALE_T', 'Memory': 'MEMORY', 'Col_block': 'COL_BLOCK', 'Method': 'METHOD'}
        self._subsections = {'MP2_INFO': 'MP2_INFO', 'RI_RPA': 'RI_RPA', 'WFC_GPW': 'WFC_GPW', 'RI_LAPLACE': 'RI_LAPLACE', 'RI_MP2': 'RI_MP2', 'CPHF': 'CPHF', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'OPT_RI_BASIS': 'OPT_RI_BASIS', 'DIRECT_CANONICAL': 'DIRECT_CANONICAL'}
        self._aliases = {'Row_block_size': 'Row_block', 'Number_proc': 'Group_size', 'Col_block_size': 'Col_block', 'Calc_condition_number': 'Calc_cond_num'}


    @property
    def Number_proc(self):
        """
        See documentation for Group_size
        """
        return self.Group_size

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

    @Number_proc.setter
    def Number_proc(self, value):
        self.Group_size = value

    @Row_block_size.setter
    def Row_block_size(self, value):
        self.Row_block = value

    @Col_block_size.setter
    def Col_block_size(self, value):
        self.Col_block = value

    @Calc_condition_number.setter
    def Calc_condition_number(self, value):
        self.Calc_cond_num = value
