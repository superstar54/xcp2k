from xcp2k.inputsection import InputSection
from xcp2k.classes._scf2 import _scf2
from xcp2k.classes._localize9 import _localize9
from xcp2k.classes._print50 import _print50


class _xas1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Method = None
        self.Xas_core = None
        self.Xas_tot_el = None
        self.Xes_core = None
        self.Xes_empty_homo = None
        self.Dipole_form = None
        self.State_type = None
        self.State_search = None
        self.Spin_channel = None
        self.Atoms_list = []
        self.At_list = self.Atoms_list
        self.Overlap_threshold = None
        self.Orbital_list = []
        self.Orbital_list = []
        self.Added_mos = None
        self.Max_iter_added = None
        self.Eps_added = None
        self.Ngauss = None
        self.Restart = None
        self.Wfn_restart_file_name = None
        self.SCF = _scf2()
        self.LOCALIZE = _localize9()
        self.PRINT = _print50()
        self._name = "XAS"
        self._keywords = {'Method': 'METHOD', 'Xas_core': 'XAS_CORE', 'Xas_tot_el': 'XAS_TOT_EL', 'Xes_core': 'XES_CORE', 'Xes_empty_homo': 'XES_EMPTY_HOMO', 'Dipole_form': 'DIPOLE_FORM', 'State_type': 'STATE_TYPE', 'State_search': 'STATE_SEARCH', 'Spin_channel': 'SPIN_CHANNEL', 'Overlap_threshold': 'OVERLAP_THRESHOLD', 'Added_mos': 'ADDED_MOS', 'Max_iter_added': 'MAX_ITER_ADDED', 'Eps_added': 'EPS_ADDED', 'Ngauss': 'NGAUSS', 'Restart': 'RESTART', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME'}
        self._repeated_keywords = {'Atoms_list': 'ATOMS_LIST', 'Orbital_list': 'ORBITAL_LIST'}
        self._subsections = {'SCF': 'SCF', 'LOCALIZE': 'LOCALIZE', 'PRINT': 'PRINT'}
        self._aliases = {'Xas_method': 'Method', 'Dip_form': 'Dipole_form', 'Type': 'State_type', 'Restart_file_name': 'Wfn_restart_file_name'}
        self._repeated_aliases = {'At_list': 'Atoms_list'}
        self._attributes = ['Section_parameters']


    @property
    def Xas_method(self):
        """
        See documentation for Method
        """
        return self.Method

    @property
    def Dip_form(self):
        """
        See documentation for Dipole_form
        """
        return self.Dipole_form

    @property
    def Type(self):
        """
        See documentation for State_type
        """
        return self.State_type

    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Xas_method.setter
    def Xas_method(self, value):
        self.Method = value

    @Dip_form.setter
    def Dip_form(self, value):
        self.Dipole_form = value

    @Type.setter
    def Type(self, value):
        self.State_type = value

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
