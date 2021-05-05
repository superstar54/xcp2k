from xcp2k.inputsection import InputSection
from xcp2k.classes._each381 import _each381


class _moments1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Periodic = None
        self.Reference = None
        self.Reference_point = None
        self.Max_moment = None
        self.Magnetic = None
        self.Vel_reprs = None
        self.Com_nl = None
        self.Second_reference_point = None
        self.Reference_2 = None
        self.Reference_point_2 = None
        self.EACH = _each381()
        self._name = "MOMENTS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Periodic': 'PERIODIC', 'Reference': 'REFERENCE', 'Reference_point': 'REFERENCE_POINT', 'Max_moment': 'MAX_MOMENT', 'Magnetic': 'MAGNETIC', 'Vel_reprs': 'VEL_REPRS', 'Com_nl': 'COM_NL', 'Second_reference_point': 'SECOND_REFERENCE_POINT', 'Reference_2': 'REFERENCE_2', 'Reference_point_2': 'REFERENCE_POINT_2'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Ref': 'Reference', 'Ref_point': 'Reference_point', 'Ref_2': 'Reference_2', 'Ref_point_2': 'Reference_point_2'}
        self._attributes = ['Section_parameters']


    @property
    def Ref(self):
        """
        See documentation for Reference
        """
        return self.Reference

    @property
    def Ref_point(self):
        """
        See documentation for Reference_point
        """
        return self.Reference_point

    @property
    def Ref_2(self):
        """
        See documentation for Reference_2
        """
        return self.Reference_2

    @property
    def Ref_point_2(self):
        """
        See documentation for Reference_point_2
        """
        return self.Reference_point_2

    @Ref.setter
    def Ref(self, value):
        self.Reference = value

    @Ref_point.setter
    def Ref_point(self, value):
        self.Reference_point = value

    @Ref_2.setter
    def Ref_2(self, value):
        self.Reference_2 = value

    @Ref_point_2.setter
    def Ref_point_2(self, value):
        self.Reference_point_2 = value
