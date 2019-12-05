from xcp2k.inputsection import InputSection
from xcp2k.classes._each233 import _each233


class _mo1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Cartesian = None
        self.Eigenvalues = None
        self.Eigenvectors = None
        self.Occupation_numbers = None
        self.Ndigits = None
        self.Mo_index_range = None
        self.EACH = _each233()
        self._name = "MO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Cartesian': 'CARTESIAN', 'Eigenvalues': 'EIGENVALUES', 'Eigenvectors': 'EIGENVECTORS', 'Occupation_numbers': 'OCCUPATION_NUMBERS', 'Ndigits': 'NDIGITS', 'Mo_index_range': 'MO_INDEX_RANGE'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Eigvals': 'Eigenvalues', 'Eigvecs': 'Eigenvectors', 'Occnums': 'Occupation_numbers', 'Mo_range': 'Mo_index_range', 'Range': 'Mo_index_range'}
        self._attributes = ['Section_parameters']


    @property
    def Eigvals(self):
        """
        See documentation for Eigenvalues
        """
        return self.Eigenvalues

    @property
    def Eigvecs(self):
        """
        See documentation for Eigenvectors
        """
        return self.Eigenvectors

    @property
    def Occnums(self):
        """
        See documentation for Occupation_numbers
        """
        return self.Occupation_numbers

    @property
    def Mo_range(self):
        """
        See documentation for Mo_index_range
        """
        return self.Mo_index_range

    @property
    def Range(self):
        """
        See documentation for Mo_index_range
        """
        return self.Mo_index_range

    @Eigvals.setter
    def Eigvals(self, value):
        self.Eigenvalues = value

    @Eigvecs.setter
    def Eigvecs(self, value):
        self.Eigenvectors = value

    @Occnums.setter
    def Occnums(self, value):
        self.Occupation_numbers = value

    @Mo_range.setter
    def Mo_range(self, value):
        self.Mo_index_range = value

    @Range.setter
    def Range(self, value):
        self.Mo_index_range = value
