from xcp2k.inputsection import InputSection
from xcp2k.classes._cphf4 import _cphf4


class _ri_mp24(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Block_size = None
        self.Eps_canonical = None
        self.Free_hfx_buffer = None
        self.CPHF = _cphf4()
        self._name = "RI_MP2"
        self._keywords = {'Block_size': 'BLOCK_SIZE', 'Eps_canonical': 'EPS_CANONICAL', 'Free_hfx_buffer': 'FREE_HFX_BUFFER'}
        self._subsections = {'CPHF': 'CPHF'}
        self._aliases = {'Message_size': 'Block_size'}
        self._attributes = ['Section_parameters']


    @property
    def Message_size(self):
        """
        See documentation for Block_size
        """
        return self.Block_size

    @Message_size.setter
    def Message_size(self, value):
        self.Block_size = value
