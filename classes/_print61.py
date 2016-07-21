from xcp2k.inputsection import InputSection
from _program_banner4 import _program_banner4
from _method_info1 import _method_info1
from _basis_set1 import _basis_set1
from _potential3 import _potential3
from _fit_density1 import _fit_density1
from _fit_kgpot1 import _fit_kgpot1
from _response_basis1 import _response_basis1
from _scf_info1 import _scf_info1
from _orbitals1 import _orbitals1
from _fit_pseudo1 import _fit_pseudo1
from _fit_basis1 import _fit_basis1
from _upf_file1 import _upf_file1
from _energies_minus_kinetic1 import _energies_minus_kinetic1


class _print61(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_BANNER = _program_banner4()
        self.METHOD_INFO = _method_info1()
        self.BASIS_SET = _basis_set1()
        self.POTENTIAL = _potential3()
        self.FIT_DENSITY = _fit_density1()
        self.FIT_KGPOT = _fit_kgpot1()
        self.RESPONSE_BASIS = _response_basis1()
        self.SCF_INFO = _scf_info1()
        self.ORBITALS = _orbitals1()
        self.FIT_PSEUDO = _fit_pseudo1()
        self.FIT_BASIS = _fit_basis1()
        self.UPF_FILE = _upf_file1()
        self.ENERGIES_MINUS_KINETIC = _energies_minus_kinetic1()
        self._name = "PRINT"
        self._subsections = {'FIT_BASIS': 'FIT_BASIS', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'RESPONSE_BASIS': 'RESPONSE_BASIS', 'ORBITALS': 'ORBITALS', 'FIT_PSEUDO': 'FIT_PSEUDO', 'ENERGIES_MINUS_KINETIC': 'ENERGIES_MINUS_KINETIC', 'POTENTIAL': 'POTENTIAL', 'FIT_KGPOT': 'FIT_KGPOT', 'BASIS_SET': 'BASIS_SET', 'FIT_DENSITY': 'FIT_DENSITY', 'UPF_FILE': 'UPF_FILE', 'METHOD_INFO': 'METHOD_INFO', 'SCF_INFO': 'SCF_INFO'}

