from xcp2k.inputsection import InputSection
from xcp2k.classes._hf8 import _hf8
from xcp2k.classes._ri_g0w04 import _ri_g0w04
from xcp2k.classes._im_time4 import _im_time4
from xcp2k.classes._ri_axk4 import _ri_axk4


class _ri_rpa4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Quadrature_points = None
        self.Size_freq_integ_group = None
        self.Mm_style = None
        self.Minimax_quadrature = None
        self.Ri_g0w0 = None
        self.Ri_axk = None
        self.Admm = None
        self.Im_time = None
        self.HF_list = []
        self.RI_G0W0 = _ri_g0w04()
        self.IM_TIME = _im_time4()
        self.RI_AXK = _ri_axk4()
        self._name = "RI_RPA"
        self._keywords = {'Quadrature_points': 'QUADRATURE_POINTS', 'Size_freq_integ_group': 'SIZE_FREQ_INTEG_GROUP', 'Mm_style': 'MM_STYLE', 'Minimax_quadrature': 'MINIMAX_QUADRATURE', 'Ri_g0w0': 'RI_G0W0', 'Ri_axk': 'RI_AXK', 'Admm': 'ADMM', 'Im_time': 'IM_TIME'}
        self._subsections = {'RI_G0W0': 'RI_G0W0', 'IM_TIME': 'IM_TIME', 'RI_AXK': 'RI_AXK'}
        self._repeated_subsections = {'HF': '_hf8'}
        self._aliases = {'Rpa_num_quad_points': 'Quadrature_points', 'Rpa_group_size': 'Size_freq_integ_group', 'Minimax': 'Minimax_quadrature', 'Gw': 'Ri_g0w0', 'Axk': 'Ri_axk', 'Imag_time': 'Im_time'}
        self._attributes = ['HF_list']

    def HF_add(self, section_parameters=None):
        new_section = _hf8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section


    @property
    def Rpa_num_quad_points(self):
        """
        See documentation for Quadrature_points
        """
        return self.Quadrature_points

    @property
    def Rpa_group_size(self):
        """
        See documentation for Size_freq_integ_group
        """
        return self.Size_freq_integ_group

    @property
    def Minimax(self):
        """
        See documentation for Minimax_quadrature
        """
        return self.Minimax_quadrature

    @property
    def Gw(self):
        """
        See documentation for Ri_g0w0
        """
        return self.Ri_g0w0

    @property
    def Axk(self):
        """
        See documentation for Ri_axk
        """
        return self.Ri_axk

    @property
    def Imag_time(self):
        """
        See documentation for Im_time
        """
        return self.Im_time

    @Rpa_num_quad_points.setter
    def Rpa_num_quad_points(self, value):
        self.Quadrature_points = value

    @Rpa_group_size.setter
    def Rpa_group_size(self, value):
        self.Size_freq_integ_group = value

    @Minimax.setter
    def Minimax(self, value):
        self.Minimax_quadrature = value

    @Gw.setter
    def Gw(self, value):
        self.Ri_g0w0 = value

    @Axk.setter
    def Axk(self, value):
        self.Ri_axk = value

    @Imag_time.setter
    def Imag_time(self, value):
        self.Im_time = value
