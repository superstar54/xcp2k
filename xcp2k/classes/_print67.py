from xcp2k.inputsection import InputSection
from xcp2k.classes._guess_vectors1 import _guess_vectors1
from xcp2k.classes._iteration_info4 import _iteration_info4
from xcp2k.classes._detailed_energy3 import _detailed_energy3
from xcp2k.classes._restart13 import _restart13


class _print67(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.GUESS_VECTORS = _guess_vectors1()
        self.ITERATION_INFO = _iteration_info4()
        self.DETAILED_ENERGY = _detailed_energy3()
        self.RESTART = _restart13()
        self._name = "PRINT"
        self._subsections = {'GUESS_VECTORS': 'GUESS_VECTORS', 'ITERATION_INFO': 'ITERATION_INFO', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'RESTART': 'RESTART'}

