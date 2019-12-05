from xcp2k.inputsection import InputSection
from xcp2k.classes._xc3 import _xc3
from xcp2k.classes._sic1 import _sic1


class _tddfpt1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_kv = None
        self.Restarts = None
        self.Nev = None
        self.Nlumo = None
        self.Nreortho = None
        self.Kernel = None
        self.Lsd_singlets = None
        self.Invert_s = None
        self.Preconditioner = None
        self.Res_etype = None
        self.Diag_method = None
        self.Oe_corr = None
        self.Convergence = None
        self.XC = _xc3()
        self.SIC = _sic1()
        self._name = "TDDFPT"
        self._keywords = {'Max_kv': 'MAX_KV', 'Restarts': 'RESTARTS', 'Nev': 'NEV', 'Nlumo': 'NLUMO', 'Nreortho': 'NREORTHO', 'Kernel': 'KERNEL', 'Lsd_singlets': 'LSD_SINGLETS', 'Invert_s': 'INVERT_S', 'Preconditioner': 'PRECONDITIONER', 'Res_etype': 'RES_ETYPE', 'Diag_method': 'DIAG_METHOD', 'Oe_corr': 'OE_CORR', 'Convergence': 'CONVERGENCE'}
        self._subsections = {'XC': 'XC', 'SIC': 'SIC'}
        self._aliases = {'Max_vectors': 'Max_kv', 'N_restarts': 'Restarts', 'N_ev': 'Nev', 'Ev': 'Nev', 'N_reortho': 'Nreortho', 'Reortho': 'Nreortho', 'Reorthogonalitazions': 'Nreortho', 'Do_kernel': 'Kernel', 'Invert_overlap': 'Invert_s', 'Precond': 'Preconditioner', 'Restricted_excitations_type': 'Res_etype', 'Res_e_type': 'Res_etype', 'Diagonalization_method': 'Diag_method', 'Method': 'Diag_method', 'Orbital_eigenvalues_correction': 'Oe_corr', 'Conv': 'Convergence'}


    @property
    def Max_vectors(self):
        """
        See documentation for Max_kv
        """
        return self.Max_kv

    @property
    def N_restarts(self):
        """
        See documentation for Restarts
        """
        return self.Restarts

    @property
    def N_ev(self):
        """
        See documentation for Nev
        """
        return self.Nev

    @property
    def Ev(self):
        """
        See documentation for Nev
        """
        return self.Nev

    @property
    def N_reortho(self):
        """
        See documentation for Nreortho
        """
        return self.Nreortho

    @property
    def Reortho(self):
        """
        See documentation for Nreortho
        """
        return self.Nreortho

    @property
    def Reorthogonalitazions(self):
        """
        See documentation for Nreortho
        """
        return self.Nreortho

    @property
    def Do_kernel(self):
        """
        See documentation for Kernel
        """
        return self.Kernel

    @property
    def Invert_overlap(self):
        """
        See documentation for Invert_s
        """
        return self.Invert_s

    @property
    def Precond(self):
        """
        See documentation for Preconditioner
        """
        return self.Preconditioner

    @property
    def Restricted_excitations_type(self):
        """
        See documentation for Res_etype
        """
        return self.Res_etype

    @property
    def Res_e_type(self):
        """
        See documentation for Res_etype
        """
        return self.Res_etype

    @property
    def Diagonalization_method(self):
        """
        See documentation for Diag_method
        """
        return self.Diag_method

    @property
    def Method(self):
        """
        See documentation for Diag_method
        """
        return self.Diag_method

    @property
    def Orbital_eigenvalues_correction(self):
        """
        See documentation for Oe_corr
        """
        return self.Oe_corr

    @property
    def Conv(self):
        """
        See documentation for Convergence
        """
        return self.Convergence

    @Max_vectors.setter
    def Max_vectors(self, value):
        self.Max_kv = value

    @N_restarts.setter
    def N_restarts(self, value):
        self.Restarts = value

    @N_ev.setter
    def N_ev(self, value):
        self.Nev = value

    @Ev.setter
    def Ev(self, value):
        self.Nev = value

    @N_reortho.setter
    def N_reortho(self, value):
        self.Nreortho = value

    @Reortho.setter
    def Reortho(self, value):
        self.Nreortho = value

    @Reorthogonalitazions.setter
    def Reorthogonalitazions(self, value):
        self.Nreortho = value

    @Do_kernel.setter
    def Do_kernel(self, value):
        self.Kernel = value

    @Invert_overlap.setter
    def Invert_overlap(self, value):
        self.Invert_s = value

    @Precond.setter
    def Precond(self, value):
        self.Preconditioner = value

    @Restricted_excitations_type.setter
    def Restricted_excitations_type(self, value):
        self.Res_etype = value

    @Res_e_type.setter
    def Res_e_type(self, value):
        self.Res_etype = value

    @Diagonalization_method.setter
    def Diagonalization_method(self, value):
        self.Diag_method = value

    @Method.setter
    def Method(self, value):
        self.Diag_method = value

    @Orbital_eigenvalues_correction.setter
    def Orbital_eigenvalues_correction(self, value):
        self.Oe_corr = value

    @Conv.setter
    def Conv(self, value):
        self.Convergence = value
