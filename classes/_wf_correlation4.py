from xcp2k.inputsection import InputSection
from _mp2_info4 import _mp2_info4
from _direct_canonical4 import _direct_canonical4
from _wfc_gpw4 import _wfc_gpw4
from _ri_mp24 import _ri_mp24
from _opt_ri_basis4 import _opt_ri_basis4
from _ri_rpa4 import _ri_rpa4
from _ri_laplace4 import _ri_laplace4
from _cphf4 import _cphf4
from _interaction_potential12 import _interaction_potential12


class _wf_correlation4(InputSection):
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
        self.MP2_INFO = _mp2_info4()
        self.DIRECT_CANONICAL = _direct_canonical4()
        self.WFC_GPW = _wfc_gpw4()
        self.RI_MP2 = _ri_mp24()
        self.OPT_RI_BASIS = _opt_ri_basis4()
        self.RI_RPA = _ri_rpa4()
        self.RI_LAPLACE = _ri_laplace4()
        self.CPHF = _cphf4()
        self.INTERACTION_POTENTIAL = _interaction_potential12()
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
