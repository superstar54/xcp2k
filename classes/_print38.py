from xcp2k.inputsection import InputSection
from _dipole4 import _dipole4
from _pgf1 import _pgf1
from _potential1 import _potential1
from _mm_potential1 import _mm_potential1
from _qmmm_matrix1 import _qmmm_matrix1
from _program_banner3 import _program_banner3
from _program_run_info30 import _program_run_info30
from _periodic_info1 import _periodic_info1
from _grid_information2 import _grid_information2
from _derivatives3 import _derivatives3
from _qmmm_charges1 import _qmmm_charges1
from _qmmm_link_info1 import _qmmm_link_info1
from _qs_derivatives1 import _qs_derivatives1
from _image_charge_info1 import _image_charge_info1
from _image_charge_restart1 import _image_charge_restart1


class _print38(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DIPOLE = _dipole4()
        self.PGF = _pgf1()
        self.POTENTIAL = _potential1()
        self.MM_POTENTIAL = _mm_potential1()
        self.QMMM_MATRIX = _qmmm_matrix1()
        self.PROGRAM_BANNER = _program_banner3()
        self.PROGRAM_RUN_INFO = _program_run_info30()
        self.PERIODIC_INFO = _periodic_info1()
        self.GRID_INFORMATION = _grid_information2()
        self.DERIVATIVES = _derivatives3()
        self.QMMM_CHARGES = _qmmm_charges1()
        self.QMMM_LINK_INFO = _qmmm_link_info1()
        self.QS_DERIVATIVES = _qs_derivatives1()
        self.IMAGE_CHARGE_INFO = _image_charge_info1()
        self.IMAGE_CHARGE_RESTART = _image_charge_restart1()
        self._name = "PRINT"
        self._subsections = {'PGF': 'PGF', 'DERIVATIVES': 'DERIVATIVES', 'IMAGE_CHARGE_RESTART': 'IMAGE_CHARGE_RESTART', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'DIPOLE': 'DIPOLE', 'QMMM_CHARGES': 'QMMM_CHARGES', 'QMMM_MATRIX': 'QMMM_MATRIX', 'QMMM_LINK_INFO': 'QMMM_LINK_INFO', 'POTENTIAL': 'POTENTIAL', 'IMAGE_CHARGE_INFO': 'IMAGE_CHARGE_INFO', 'GRID_INFORMATION': 'GRID_INFORMATION', 'MM_POTENTIAL': 'MM_POTENTIAL', 'PERIODIC_INFO': 'PERIODIC_INFO', 'QS_DERIVATIVES': 'QS_DERIVATIVES'}

