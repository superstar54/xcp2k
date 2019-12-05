from xcp2k.inputsection import InputSection
from xcp2k.classes._ub1 import _ub1


class _bend1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Cb = None
        self.R012 = None
        self.R032 = None
        self.Kbs12 = None
        self.Kbs32 = None
        self.Kss = None
        self.Theta0 = None
        self.Legendre = None
        self.UB = _ub1()
        self._name = "BEND"
        self._keywords = {'Atoms': 'ATOMS', 'Kind': 'KIND', 'K': 'K', 'Cb': 'CB', 'R012': 'R012', 'R032': 'R032', 'Kbs12': 'KBS12', 'Kbs32': 'KBS32', 'Kss': 'KSS', 'Theta0': 'THETA0', 'Legendre': 'LEGENDRE'}
        self._subsections = {'UB': 'UB'}

