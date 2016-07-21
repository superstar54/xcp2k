from xcp2k.inputsection import InputSection
from _ot1 import _ot1
from _diagonalization1 import _diagonalization1
from _outer_scf1 import _outer_scf1
from _smear1 import _smear1
from _mixing2 import _mixing2
from _print18 import _print18


class _scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter_lumo = None
        self.Eps_lumo = None
        self.Max_scf = None
        self.Max_scf_history = None
        self.Max_diis = None
        self.Level_shift = None
        self.Eps_scf = None
        self.Eps_scf_history = None
        self.Cholesky = None
        self.Eps_eigval = None
        self.Eps_diis = None
        self.Scf_guess = None
        self.Nrow_block = None
        self.Ncol_block = None
        self.Added_mos = None
        self.Roks_scheme = None
        self.Roks_f = None
        self.Roks_parameters = None
        self.OT = _ot1()
        self.DIAGONALIZATION = _diagonalization1()
        self.OUTER_SCF = _outer_scf1()
        self.SMEAR = _smear1()
        self.MIXING = _mixing2()
        self.PRINT = _print18()
        self._name = "SCF"
        self._keywords = {'Roks_scheme': 'ROKS_SCHEME', 'Cholesky': 'CHOLESKY', 'Max_scf_history': 'MAX_SCF_HISTORY', 'Level_shift': 'LEVEL_SHIFT', 'Added_mos': 'ADDED_MOS', 'Max_diis': 'MAX_DIIS', 'Roks_f': 'ROKS_F', 'Ncol_block': 'NCOL_BLOCK', 'Eps_diis': 'EPS_DIIS', 'Max_iter_lumo': 'MAX_ITER_LUMO', 'Eps_scf': 'EPS_SCF', 'Nrow_block': 'NROW_BLOCK', 'Roks_parameters': 'ROKS_PARAMETERS', 'Max_scf': 'MAX_SCF', 'Eps_scf_history': 'EPS_SCF_HISTORY', 'Scf_guess': 'SCF_GUESS', 'Eps_lumo': 'EPS_LUMO', 'Eps_eigval': 'EPS_EIGVAL'}
        self._subsections = {'SMEAR': 'SMEAR', 'OUTER_SCF': 'OUTER_SCF', 'PRINT': 'PRINT', 'MIXING': 'MIXING', 'DIAGONALIZATION': 'DIAGONALIZATION', 'OT': 'OT'}
        self._aliases = {'Max_iter_lumos': 'Max_iter_lumo', 'F_roks': 'Roks_f', 'Max_scf_hist': 'Max_scf_history', 'Eps_lumos': 'Eps_lumo', 'Roks_parameter': 'Roks_parameters', 'Eps_scf_hist': 'Eps_scf_history', 'Max_diis_buffer_size': 'Max_diis', 'Lshift': 'Level_shift'}


    @property
    def Max_iter_lumos(self):
        """
        See documentation for Max_iter_lumo
        """
        return self.Max_iter_lumo

    @property
    def Eps_lumos(self):
        """
        See documentation for Eps_lumo
        """
        return self.Eps_lumo

    @property
    def Max_scf_hist(self):
        """
        See documentation for Max_scf_history
        """
        return self.Max_scf_history

    @property
    def Max_diis_buffer_size(self):
        """
        See documentation for Max_diis
        """
        return self.Max_diis

    @property
    def Lshift(self):
        """
        See documentation for Level_shift
        """
        return self.Level_shift

    @property
    def Eps_scf_hist(self):
        """
        See documentation for Eps_scf_history
        """
        return self.Eps_scf_history

    @property
    def F_roks(self):
        """
        See documentation for Roks_f
        """
        return self.Roks_f

    @property
    def Roks_parameter(self):
        """
        See documentation for Roks_parameters
        """
        return self.Roks_parameters

    @Max_iter_lumos.setter
    def Max_iter_lumos(self, value):
        self.Max_iter_lumo = value

    @Eps_lumos.setter
    def Eps_lumos(self, value):
        self.Eps_lumo = value

    @Max_scf_hist.setter
    def Max_scf_hist(self, value):
        self.Max_scf_history = value

    @Max_diis_buffer_size.setter
    def Max_diis_buffer_size(self, value):
        self.Max_diis = value

    @Lshift.setter
    def Lshift(self, value):
        self.Level_shift = value

    @Eps_scf_hist.setter
    def Eps_scf_hist(self, value):
        self.Eps_scf_history = value

    @F_roks.setter
    def F_roks(self, value):
        self.Roks_f = value

    @Roks_parameter.setter
    def Roks_parameter(self, value):
        self.Roks_parameters = value
