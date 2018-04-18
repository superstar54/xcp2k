from xcp2k.inputsection import InputSection


class _mixing1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Method = None
        self.Alpha = None
        self.Beta = None
        self.Pulay_alpha = None
        self.Pulay_beta = None
        self.Nmixing = None
        self.Nbuffer = None
        self.Broy_w0 = None
        self.Broy_wref = None
        self.Broy_wmax = None
        self.Regularization = None
        self.Max_step = None
        self.R_factor = None
        self.Nskip = None
        self.N_simple_mix = None
        self.Max_gvec_exp = None
        self.Gmix_p = None
        self._name = "MIXING"
        self._keywords = {'Regularization': 'REGULARIZATION', 'Max_step': 'MAX_STEP', 'R_factor': 'R_FACTOR', 'Pulay_beta': 'PULAY_BETA', 'Broy_w0': 'BROY_W0', 'Max_gvec_exp': 'MAX_GVEC_EXP', 'Nbuffer': 'NBUFFER', 'Broy_wref': 'BROY_WREF', 'Nskip': 'NSKIP', 'Beta': 'BETA', 'Pulay_alpha': 'PULAY_ALPHA', 'N_simple_mix': 'N_SIMPLE_MIX', 'Broy_wmax': 'BROY_WMAX', 'Alpha': 'ALPHA', 'Nmixing': 'NMIXING', 'Gmix_p': 'GMIX_P', 'Method': 'METHOD'}
        self._aliases = {'Nskip_mixing': 'Nskip', 'Nsimplemix': 'N_simple_mix', 'Nmultisecant': 'Nbuffer', 'Npulay': 'Nbuffer', 'Nbroyden': 'Nbuffer'}
        self._attributes = ['Section_parameters']


    @property
    def Npulay(self):
        """
        See documentation for Nbuffer
        """
        return self.Nbuffer

    @property
    def Nbroyden(self):
        """
        See documentation for Nbuffer
        """
        return self.Nbuffer

    @property
    def Nmultisecant(self):
        """
        See documentation for Nbuffer
        """
        return self.Nbuffer

    @property
    def Nskip_mixing(self):
        """
        See documentation for Nskip
        """
        return self.Nskip

    @property
    def Nsimplemix(self):
        """
        See documentation for N_simple_mix
        """
        return self.N_simple_mix

    @Npulay.setter
    def Npulay(self, value):
        self.Nbuffer = value

    @Nbroyden.setter
    def Nbroyden(self, value):
        self.Nbuffer = value

    @Nmultisecant.setter
    def Nmultisecant(self, value):
        self.Nbuffer = value

    @Nskip_mixing.setter
    def Nskip_mixing(self, value):
        self.Nskip = value

    @Nsimplemix.setter
    def Nsimplemix(self, value):
        self.N_simple_mix = value
