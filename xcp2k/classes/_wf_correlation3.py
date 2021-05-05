from xcp2k.inputsection import InputSection
from xcp2k.classes._mp23 import _mp23
from xcp2k.classes._ri_mp23 import _ri_mp23
from xcp2k.classes._ri_rpa3 import _ri_rpa3
from xcp2k.classes._ri_sos_mp23 import _ri_sos_mp23
from xcp2k.classes._low_scaling3 import _low_scaling3
from xcp2k.classes._ri9 import _ri9
from xcp2k.classes._integrals3 import _integrals3


class _wf_correlation3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Memory = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.MP2 = _mp23()
        self.RI_MP2 = _ri_mp23()
        self.RI_RPA = _ri_rpa3()
        self.RI_SOS_MP2 = _ri_sos_mp23()
        self.LOW_SCALING = _low_scaling3()
        self.RI = _ri9()
        self.INTEGRALS = _integrals3()
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
