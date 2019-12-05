from xcp2k.inputsection import InputSection
from xcp2k.classes._mode_selective1 import _mode_selective1
from xcp2k.classes._print71 import _print71


class _vibrational_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dx = None
        self.Nproc_rep = None
        self.Proc_dist_type = None
        self.Fully_periodic = None
        self.Intensities = None
        self.Thermochemistry = None
        self.Tc_temperature = None
        self.Tc_pressure = None
        self.MODE_SELECTIVE = _mode_selective1()
        self.PRINT = _print71()
        self._name = "VIBRATIONAL_ANALYSIS"
        self._keywords = {'Dx': 'DX', 'Nproc_rep': 'NPROC_REP', 'Proc_dist_type': 'PROC_DIST_TYPE', 'Fully_periodic': 'FULLY_PERIODIC', 'Intensities': 'INTENSITIES', 'Thermochemistry': 'THERMOCHEMISTRY', 'Tc_temperature': 'TC_TEMPERATURE', 'Tc_pressure': 'TC_PRESSURE'}
        self._subsections = {'MODE_SELECTIVE': 'MODE_SELECTIVE', 'PRINT': 'PRINT'}

