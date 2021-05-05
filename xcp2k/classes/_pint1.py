from xcp2k.inputsection import InputSection
from xcp2k.classes._normalmode1 import _normalmode1
from xcp2k.classes._staging1 import _staging1
from xcp2k.classes._beads1 import _beads1
from xcp2k.classes._nose6 import _nose6
from xcp2k.classes._gle4 import _gle4
from xcp2k.classes._pile1 import _pile1
from xcp2k.classes._piglet1 import _piglet1
from xcp2k.classes._qtb1 import _qtb1
from xcp2k.classes._init1 import _init1
from xcp2k.classes._helium1 import _helium1
from xcp2k.classes._print15 import _print15


class _pint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.P = None
        self.Proc_per_replica = None
        self.Num_steps = None
        self.Max_step = None
        self.Iteration = None
        self.Temp = None
        self.Kt_correction = None
        self.T_tol = None
        self.Dt = None
        self.Harm_int = None
        self.Nrespa = None
        self.Transformation = None
        self.Propagator = None
        self.Fix_centroid_pos = None
        self.NORMALMODE = _normalmode1()
        self.STAGING = _staging1()
        self.BEADS = _beads1()
        self.NOSE = _nose6()
        self.GLE = _gle4()
        self.PILE = _pile1()
        self.PIGLET = _piglet1()
        self.QTB = _qtb1()
        self.INIT = _init1()
        self.HELIUM = _helium1()
        self.PRINT = _print15()
        self._name = "PINT"
        self._keywords = {'P': 'P', 'Proc_per_replica': 'PROC_PER_REPLICA', 'Num_steps': 'NUM_STEPS', 'Max_step': 'MAX_STEP', 'Iteration': 'ITERATION', 'Temp': 'TEMP', 'Kt_correction': 'KT_CORRECTION', 'T_tol': 'T_TOL', 'Dt': 'DT', 'Harm_int': 'HARM_INT', 'Nrespa': 'NRESPA', 'Transformation': 'TRANSFORMATION', 'Propagator': 'PROPAGATOR', 'Fix_centroid_pos': 'FIX_CENTROID_POS'}
        self._subsections = {'NORMALMODE': 'NORMALMODE', 'STAGING': 'STAGING', 'BEADS': 'BEADS', 'NOSE': 'NOSE', 'GLE': 'GLE', 'PILE': 'PILE', 'PIGLET': 'PIGLET', 'QTB': 'QTB', 'INIT': 'INIT', 'HELIUM': 'HELIUM', 'PRINT': 'PRINT'}
        self._aliases = {'Temp_to': 'T_tol'}


    @property
    def Temp_to(self):
        """
        See documentation for T_tol
        """
        return self.T_tol

    @Temp_to.setter
    def Temp_to(self, value):
        self.T_tol = value
