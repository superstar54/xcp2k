from xcp2k.inputsection import InputSection
from xcp2k.classes._dipole_moments1 import _dipole_moments1
from xcp2k.classes._xc6 import _xc6
from xcp2k.classes._mgrid2 import _mgrid2
from xcp2k.classes._stda1 import _stda1
from xcp2k.classes._print91 import _print91


class _tddfpt2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Nstates = None
        self.Max_iter = None
        self.Max_kv = None
        self.Nlumo = None
        self.Nproc_state = None
        self.Kernel = None
        self.Oe_corr = None
        self.Ev_shift = None
        self.Eos_shift = None
        self.Convergence = None
        self.Min_amplitude = None
        self.Orthogonal_eps = None
        self.Restart = None
        self.Rks_triplets = None
        self.Wfn_restart_file_name = None
        self.DIPOLE_MOMENTS = _dipole_moments1()
        self.XC = _xc6()
        self.MGRID = _mgrid2()
        self.STDA = _stda1()
        self.PRINT = _print91()
        self._name = "TDDFPT"
        self._keywords = {'Nstates': 'NSTATES', 'Max_iter': 'MAX_ITER', 'Max_kv': 'MAX_KV', 'Nlumo': 'NLUMO', 'Nproc_state': 'NPROC_STATE', 'Kernel': 'KERNEL', 'Oe_corr': 'OE_CORR', 'Ev_shift': 'EV_SHIFT', 'Eos_shift': 'EOS_SHIFT', 'Convergence': 'CONVERGENCE', 'Min_amplitude': 'MIN_AMPLITUDE', 'Orthogonal_eps': 'ORTHOGONAL_EPS', 'Restart': 'RESTART', 'Rks_triplets': 'RKS_TRIPLETS', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME'}
        self._subsections = {'DIPOLE_MOMENTS': 'DIPOLE_MOMENTS', 'XC': 'XC', 'MGRID': 'MGRID', 'STDA': 'STDA', 'PRINT': 'PRINT'}
        self._aliases = {'Virtual_shift': 'Ev_shift', 'Open_shell_shift': 'Eos_shift', 'Restart_file_name': 'Wfn_restart_file_name'}
        self._attributes = ['Section_parameters']


    @property
    def Virtual_shift(self):
        """
        See documentation for Ev_shift
        """
        return self.Ev_shift

    @property
    def Open_shell_shift(self):
        """
        See documentation for Eos_shift
        """
        return self.Eos_shift

    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Virtual_shift.setter
    def Virtual_shift(self, value):
        self.Ev_shift = value

    @Open_shell_shift.setter
    def Open_shell_shift(self, value):
        self.Eos_shift = value

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
