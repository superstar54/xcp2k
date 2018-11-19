from xcp2k.inputsection import InputSection
from _mao6 import _mao6


class _im_time6(InputSection):
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
        self.MAO = _mao6()
        self._name = "IM_TIME"
        self._keywords = {'Group_size_3c': 'GROUP_SIZE_3C', 'Points_per_magnitude': 'POINTS_PER_MAGNITUDE', 'Group_size_p': 'GROUP_SIZE_P', 'Ri_g0w0': 'RI_G0W0', 'Stabilize_exp': 'STABILIZE_EXP', 'Memory_info': 'MEMORY_INFO', 'Memory_cut': 'MEMORY_CUT', 'Eps_filter_im_time': 'EPS_FILTER_IM_TIME', 'Mao': 'MAO'}
        self._subsections = {'MAO': 'MAO'}
        self._aliases = {'Gw': 'Ri_g0w0', 'Ppm': 'Points_per_magnitude'}


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
