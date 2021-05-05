from xcp2k.inputsection import InputSection
from xcp2k.classes._mp26 import _mp26
from xcp2k.classes._ri_mp26 import _ri_mp26
from xcp2k.classes._ri_rpa6 import _ri_rpa6
from xcp2k.classes._ri_sos_mp26 import _ri_sos_mp26
from xcp2k.classes._low_scaling6 import _low_scaling6
from xcp2k.classes._ri18 import _ri18
from xcp2k.classes._integrals6 import _integrals6


class _wf_correlation6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Memory = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.MP2 = _mp26()
        self.RI_MP2 = _ri_mp26()
        self.RI_RPA = _ri_rpa6()
        self.RI_SOS_MP2 = _ri_sos_mp26()
        self.LOW_SCALING = _low_scaling6()
        self.RI = _ri18()
        self.INTEGRALS = _integrals6()
        self._name = "WF_CORRELATION"
        self._keywords = {'Memory': 'MEMORY', 'Scale_s': 'SCALE_S', 'Scale_t': 'SCALE_T', 'Group_size': 'GROUP_SIZE'}
        self._subsections = {'MP2': 'MP2', 'RI_MP2': 'RI_MP2', 'RI_RPA': 'RI_RPA', 'RI_SOS_MP2': 'RI_SOS_MP2', 'LOW_SCALING': 'LOW_SCALING', 'RI': 'RI', 'INTEGRALS': 'INTEGRALS'}
        self._aliases = {'Number_proc': 'Group_size'}


    @property
    def Number_proc(self):
        """
        See documentation for Group_size
        """
        return self.Group_size

    @Number_proc.setter
    def Number_proc(self, value):
        self.Group_size = value
