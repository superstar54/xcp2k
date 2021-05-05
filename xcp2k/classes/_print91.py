from xcp2k.inputsection import InputSection
from xcp2k.classes._program_banner4 import _program_banner4
from xcp2k.classes._guess_vectors1 import _guess_vectors1
from xcp2k.classes._iteration_info4 import _iteration_info4
from xcp2k.classes._detailed_energy3 import _detailed_energy3
from xcp2k.classes._restart14 import _restart14
from xcp2k.classes._nto_analysis1 import _nto_analysis1
from xcp2k.classes._mos_molden1 import _mos_molden1


class _print91(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_BANNER = _program_banner4()
        self.GUESS_VECTORS = _guess_vectors1()
        self.ITERATION_INFO = _iteration_info4()
        self.DETAILED_ENERGY = _detailed_energy3()
        self.RESTART = _restart14()
        self.NTO_ANALYSIS = _nto_analysis1()
        self.MOS_MOLDEN = _mos_molden1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_BANNER': 'PROGRAM_BANNER', 'GUESS_VECTORS': 'GUESS_VECTORS', 'ITERATION_INFO': 'ITERATION_INFO', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'RESTART': 'RESTART', 'NTO_ANALYSIS': 'NTO_ANALYSIS', 'MOS_MOLDEN': 'MOS_MOLDEN'}

