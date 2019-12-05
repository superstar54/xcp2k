from xcp2k.inputsection import InputSection
from xcp2k.classes._program_banner4 import _program_banner4
from xcp2k.classes._method_info1 import _method_info1
from xcp2k.classes._basis_set1 import _basis_set1
from xcp2k.classes._potential3 import _potential3
from xcp2k.classes._fit_density1 import _fit_density1
from xcp2k.classes._fit_kgpot1 import _fit_kgpot1
from xcp2k.classes._response_basis1 import _response_basis1
from xcp2k.classes._geometrical_response_basis1 import _geometrical_response_basis1
from xcp2k.classes._scf_info1 import _scf_info1
from xcp2k.classes._orbitals1 import _orbitals1
from xcp2k.classes._analyze_basis1 import _analyze_basis1
from xcp2k.classes._fit_pseudo1 import _fit_pseudo1
from xcp2k.classes._fit_basis1 import _fit_basis1
from xcp2k.classes._upf_file1 import _upf_file1
from xcp2k.classes._separable_gaussian_pseudo1 import _separable_gaussian_pseudo1
from xcp2k.classes._admm1 import _admm1


class _print74(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_BANNER = _program_banner4()
        self.METHOD_INFO = _method_info1()
        self.BASIS_SET = _basis_set1()
        self.POTENTIAL = _potential3()
        self.FIT_DENSITY = _fit_density1()
        self.FIT_KGPOT = _fit_kgpot1()
        self.RESPONSE_BASIS = _response_basis1()
        self.GEOMETRICAL_RESPONSE_BASIS = _geometrical_response_basis1()
        self.SCF_INFO = _scf_info1()
        self.ORBITALS = _orbitals1()
        self.ANALYZE_BASIS = _analyze_basis1()
        self.FIT_PSEUDO = _fit_pseudo1()
        self.FIT_BASIS = _fit_basis1()
        self.UPF_FILE = _upf_file1()
        self.SEPARABLE_GAUSSIAN_PSEUDO = _separable_gaussian_pseudo1()
        self.ADMM = _admm1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_BANNER': 'PROGRAM_BANNER', 'METHOD_INFO': 'METHOD_INFO', 'BASIS_SET': 'BASIS_SET', 'POTENTIAL': 'POTENTIAL', 'FIT_DENSITY': 'FIT_DENSITY', 'FIT_KGPOT': 'FIT_KGPOT', 'RESPONSE_BASIS': 'RESPONSE_BASIS', 'GEOMETRICAL_RESPONSE_BASIS': 'GEOMETRICAL_RESPONSE_BASIS', 'SCF_INFO': 'SCF_INFO', 'ORBITALS': 'ORBITALS', 'ANALYZE_BASIS': 'ANALYZE_BASIS', 'FIT_PSEUDO': 'FIT_PSEUDO', 'FIT_BASIS': 'FIT_BASIS', 'UPF_FILE': 'UPF_FILE', 'SEPARABLE_GAUSSIAN_PSEUDO': 'SEPARABLE_GAUSSIAN_PSEUDO', 'ADMM': 'ADMM'}

