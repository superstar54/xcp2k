from xcp2k.inputsection import InputSection
from _sphere1 import _sphere1
from _program_run_info17 import _program_run_info17


class _scrf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_out = None
        self.Lmax = None
        self.SPHERE = _sphere1()
        self.PROGRAM_RUN_INFO = _program_run_info17()
        self._name = "SCRF"
        self._keywords = {'Lmax': 'LMAX', 'Eps_out': 'EPS_OUT'}
        self._subsections = {'SPHERE': 'SPHERE', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

