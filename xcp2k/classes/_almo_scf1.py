from xcp2k.inputsection import InputSection
from xcp2k.classes._almo_optimizer_diis1 import _almo_optimizer_diis1
from xcp2k.classes._almo_optimizer_pcg1 import _almo_optimizer_pcg1
from xcp2k.classes._almo_optimizer_trustr1 import _almo_optimizer_trustr1
from xcp2k.classes._xalmo_optimizer_pcg1 import _xalmo_optimizer_pcg1
from xcp2k.classes._xalmo_optimizer_trustr1 import _xalmo_optimizer_trustr1
from xcp2k.classes._nlmo_optimizer_pcg1 import _nlmo_optimizer_pcg1
from xcp2k.classes._matrix_iterate1 import _matrix_iterate1
from xcp2k.classes._analysis1 import _analysis1


class _almo_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_filter = None
        self.Almo_scf_guess = None
        self.Mo_overlap_inv_alg = None
        self.Almo_extrapolation_order = None
        self.Xalmo_extrapolation_order = None
        self.Almo_algorithm = None
        self.Xalmo_algorithm = None
        self.Xalmo_trial_wf = None
        self.Delocalize_method = None
        self.Xalmo_r_cutoff_factor = None
        self.Return_orthogonalized_mos = None
        self.Construct_nlmos = None
        self.ALMO_OPTIMIZER_DIIS = _almo_optimizer_diis1()
        self.ALMO_OPTIMIZER_PCG = _almo_optimizer_pcg1()
        self.ALMO_OPTIMIZER_TRUSTR = _almo_optimizer_trustr1()
        self.XALMO_OPTIMIZER_PCG = _xalmo_optimizer_pcg1()
        self.XALMO_OPTIMIZER_TRUSTR = _xalmo_optimizer_trustr1()
        self.NLMO_OPTIMIZER_PCG = _nlmo_optimizer_pcg1()
        self.MATRIX_ITERATE = _matrix_iterate1()
        self.ANALYSIS = _analysis1()
        self._name = "ALMO_SCF"
        self._keywords = {'Eps_filter': 'EPS_FILTER', 'Almo_scf_guess': 'ALMO_SCF_GUESS', 'Mo_overlap_inv_alg': 'MO_OVERLAP_INV_ALG', 'Almo_extrapolation_order': 'ALMO_EXTRAPOLATION_ORDER', 'Xalmo_extrapolation_order': 'XALMO_EXTRAPOLATION_ORDER', 'Almo_algorithm': 'ALMO_ALGORITHM', 'Xalmo_algorithm': 'XALMO_ALGORITHM', 'Xalmo_trial_wf': 'XALMO_TRIAL_WF', 'Delocalize_method': 'DELOCALIZE_METHOD', 'Xalmo_r_cutoff_factor': 'XALMO_R_CUTOFF_FACTOR', 'Return_orthogonalized_mos': 'RETURN_ORTHOGONALIZED_MOS', 'Construct_nlmos': 'CONSTRUCT_NLMOS'}
        self._subsections = {'ALMO_OPTIMIZER_DIIS': 'ALMO_OPTIMIZER_DIIS', 'ALMO_OPTIMIZER_PCG': 'ALMO_OPTIMIZER_PCG', 'ALMO_OPTIMIZER_TRUSTR': 'ALMO_OPTIMIZER_TRUSTR', 'XALMO_OPTIMIZER_PCG': 'XALMO_OPTIMIZER_PCG', 'XALMO_OPTIMIZER_TRUSTR': 'XALMO_OPTIMIZER_TRUSTR', 'NLMO_OPTIMIZER_PCG': 'NLMO_OPTIMIZER_PCG', 'MATRIX_ITERATE': 'MATRIX_ITERATE', 'ANALYSIS': 'ANALYSIS'}

