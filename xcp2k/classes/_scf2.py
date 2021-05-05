from xcp2k.inputsection import InputSection
from xcp2k.classes._ot3 import _ot3
from xcp2k.classes._diagonalization2 import _diagonalization2
from xcp2k.classes._outer_scf3 import _outer_scf3
from xcp2k.classes._smear2 import _smear2
from xcp2k.classes._mixing4 import _mixing4
from xcp2k.classes._mom2 import _mom2
from xcp2k.classes._print48 import _print48


class _scf2(InputSection):
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
        self.Notconv_stopall = None
        self.OT = _ot3()
        self.DIAGONALIZATION = _diagonalization2()
        self.OUTER_SCF = _outer_scf3()
        self.SMEAR = _smear2()
        self.MIXING = _mixing4()
        self.MOM = _mom2()
        self.PRINT = _print48()
        self._name = "SCF"
        self._keywords = {'Max_iter_lumo': 'MAX_ITER_LUMO', 'Eps_lumo': 'EPS_LUMO', 'Max_scf': 'MAX_SCF', 'Max_scf_history': 'MAX_SCF_HISTORY', 'Max_diis': 'MAX_DIIS', 'Level_shift': 'LEVEL_SHIFT', 'Eps_scf': 'EPS_SCF', 'Eps_scf_history': 'EPS_SCF_HISTORY', 'Cholesky': 'CHOLESKY', 'Eps_eigval': 'EPS_EIGVAL', 'Eps_diis': 'EPS_DIIS', 'Scf_guess': 'SCF_GUESS', 'Nrow_block': 'NROW_BLOCK', 'Ncol_block': 'NCOL_BLOCK', 'Added_mos': 'ADDED_MOS', 'Roks_scheme': 'ROKS_SCHEME', 'Roks_f': 'ROKS_F', 'Roks_parameters': 'ROKS_PARAMETERS', 'Notconv_stopall': 'NOTCONV_STOPALL'}
        self._subsections = {'OT': 'OT', 'DIAGONALIZATION': 'DIAGONALIZATION', 'OUTER_SCF': 'OUTER_SCF', 'SMEAR': 'SMEAR', 'MIXING': 'MIXING', 'MOM': 'MOM', 'PRINT': 'PRINT'}
        self._aliases = {'Max_iter_lumos': 'Max_iter_lumo', 'Eps_lumos': 'Eps_lumo', 'Max_scf_hist': 'Max_scf_history', 'Max_diis_buffer_size': 'Max_diis', 'Lshift': 'Level_shift', 'Eps_scf_hist': 'Eps_scf_history', 'F_roks': 'Roks_f', 'Roks_parameter': 'Roks_parameters'}


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
