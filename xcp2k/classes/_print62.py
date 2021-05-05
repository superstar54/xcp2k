from xcp2k.inputsection import InputSection
from xcp2k.classes._dipole4 import _dipole4
from xcp2k.classes._pgf1 import _pgf1
from xcp2k.classes._potential1 import _potential1
from xcp2k.classes._mm_potential1 import _mm_potential1
from xcp2k.classes._qmmm_matrix1 import _qmmm_matrix1
from xcp2k.classes._program_banner3 import _program_banner3
from xcp2k.classes._program_run_info41 import _program_run_info41
from xcp2k.classes._periodic_info1 import _periodic_info1
from xcp2k.classes._grid_information2 import _grid_information2
from xcp2k.classes._derivatives3 import _derivatives3
from xcp2k.classes._qmmm_charges1 import _qmmm_charges1
from xcp2k.classes._qmmm_link_info1 import _qmmm_link_info1
from xcp2k.classes._qs_derivatives1 import _qs_derivatives1
from xcp2k.classes._image_charge_info1 import _image_charge_info1
from xcp2k.classes._image_charge_restart1 import _image_charge_restart1


class _print62(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DIPOLE = _dipole4()
        self.PGF = _pgf1()
        self.POTENTIAL = _potential1()
        self.MM_POTENTIAL = _mm_potential1()
        self.QMMM_MATRIX = _qmmm_matrix1()
        self.PROGRAM_BANNER = _program_banner3()
        self.PROGRAM_RUN_INFO = _program_run_info41()
        self.PERIODIC_INFO = _periodic_info1()
        self.GRID_INFORMATION = _grid_information2()
        self.DERIVATIVES = _derivatives3()
        self.QMMM_CHARGES = _qmmm_charges1()
        self.QMMM_LINK_INFO = _qmmm_link_info1()
        self.QS_DERIVATIVES = _qs_derivatives1()
        self.IMAGE_CHARGE_INFO = _image_charge_info1()
        self.IMAGE_CHARGE_RESTART = _image_charge_restart1()
        self._name = "PRINT"
        self._subsections = {'DIPOLE': 'DIPOLE', 'PGF': 'PGF', 'POTENTIAL': 'POTENTIAL', 'MM_POTENTIAL': 'MM_POTENTIAL', 'QMMM_MATRIX': 'QMMM_MATRIX', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'PERIODIC_INFO': 'PERIODIC_INFO', 'GRID_INFORMATION': 'GRID_INFORMATION', 'DERIVATIVES': 'DERIVATIVES', 'QMMM_CHARGES': 'QMMM_CHARGES', 'QMMM_LINK_INFO': 'QMMM_LINK_INFO', 'QS_DERIVATIVES': 'QS_DERIVATIVES', 'IMAGE_CHARGE_INFO': 'IMAGE_CHARGE_INFO', 'IMAGE_CHARGE_RESTART': 'IMAGE_CHARGE_RESTART'}

