from xcp2k.inputsection import InputSection
from xcp2k.classes._mao4 import _mao4


class _im_time4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Memory_cut = None
        self.Memory_info = None
        self.Mao = None
        self.Group_size_3c = None
        self.Group_size_p = None
        self.Points_per_magnitude = None
        self.Eps_filter_im_time = None
        self.Stabilize_exp = None
        self.Ri_g0w0 = None
        self.MAO = _mao4()
        self._name = "IM_TIME"
        self._keywords = {'Memory_cut': 'MEMORY_CUT', 'Memory_info': 'MEMORY_INFO', 'Mao': 'MAO', 'Group_size_3c': 'GROUP_SIZE_3C', 'Group_size_p': 'GROUP_SIZE_P', 'Points_per_magnitude': 'POINTS_PER_MAGNITUDE', 'Eps_filter_im_time': 'EPS_FILTER_IM_TIME', 'Stabilize_exp': 'STABILIZE_EXP', 'Ri_g0w0': 'RI_G0W0'}
        self._subsections = {'MAO': 'MAO'}
        self._aliases = {'Ppm': 'Points_per_magnitude', 'Gw': 'Ri_g0w0'}


    @property
    def Ppm(self):
        """
        See documentation for Points_per_magnitude
        """
        return self.Points_per_magnitude

    @property
    def Gw(self):
        """
        See documentation for Ri_g0w0
        """
        return self.Ri_g0w0

    @Ppm.setter
    def Ppm(self, value):
        self.Points_per_magnitude = value

    @Gw.setter
    def Gw(self, value):
        self.Ri_g0w0 = value
