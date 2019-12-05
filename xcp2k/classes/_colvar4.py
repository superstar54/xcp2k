from xcp2k.inputsection import InputSection
from xcp2k.classes._distance4 import _distance4
from xcp2k.classes._angle5 import _angle5
from xcp2k.classes._torsion6 import _torsion6
from xcp2k.classes._coordination4 import _coordination4
from xcp2k.classes._population4 import _population4
from xcp2k.classes._gyration_radius4 import _gyration_radius4
from xcp2k.classes._distance_point_plane4 import _distance_point_plane4
from xcp2k.classes._angle_plane_plane4 import _angle_plane_plane4
from xcp2k.classes._bond_rotation4 import _bond_rotation4
from xcp2k.classes._distance_function4 import _distance_function4
from xcp2k.classes._qparm4 import _qparm4
from xcp2k.classes._hydronium_shell4 import _hydronium_shell4
from xcp2k.classes._hydronium_distance4 import _hydronium_distance4
from xcp2k.classes._acid_hydronium_distance4 import _acid_hydronium_distance4
from xcp2k.classes._acid_hydronium_shell4 import _acid_hydronium_shell4
from xcp2k.classes._rmsd4 import _rmsd4
from xcp2k.classes._xyz_diag4 import _xyz_diag4
from xcp2k.classes._xyz_outerdiag4 import _xyz_outerdiag4
from xcp2k.classes._u4 import _u4
from xcp2k.classes._wc4 import _wc4
from xcp2k.classes._hbp4 import _hbp4
from xcp2k.classes._ring_puckering4 import _ring_puckering4
from xcp2k.classes._conditioned_distance4 import _conditioned_distance4
from xcp2k.classes._print53 import _print53
from xcp2k.classes._colvar_func_info3 import _colvar_func_info3


class _colvar4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DISTANCE = _distance4()
        self.ANGLE = _angle5()
        self.TORSION = _torsion6()
        self.COORDINATION = _coordination4()
        self.POPULATION = _population4()
        self.GYRATION_RADIUS = _gyration_radius4()
        self.DISTANCE_POINT_PLANE = _distance_point_plane4()
        self.ANGLE_PLANE_PLANE = _angle_plane_plane4()
        self.BOND_ROTATION = _bond_rotation4()
        self.DISTANCE_FUNCTION = _distance_function4()
        self.QPARM = _qparm4()
        self.HYDRONIUM_SHELL = _hydronium_shell4()
        self.HYDRONIUM_DISTANCE = _hydronium_distance4()
        self.ACID_HYDRONIUM_DISTANCE = _acid_hydronium_distance4()
        self.ACID_HYDRONIUM_SHELL = _acid_hydronium_shell4()
        self.RMSD = _rmsd4()
        self.XYZ_DIAG = _xyz_diag4()
        self.XYZ_OUTERDIAG = _xyz_outerdiag4()
        self.U = _u4()
        self.WC = _wc4()
        self.HBP = _hbp4()
        self.RING_PUCKERING = _ring_puckering4()
        self.CONDITIONED_DISTANCE = _conditioned_distance4()
        self.PRINT_list = []
        self.COLVAR_FUNC_INFO = _colvar_func_info3()
        self._name = "COLVAR"
        self._subsections = {'DISTANCE': 'DISTANCE', 'ANGLE': 'ANGLE', 'TORSION': 'TORSION', 'COORDINATION': 'COORDINATION', 'POPULATION': 'POPULATION', 'GYRATION_RADIUS': 'GYRATION_RADIUS', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'BOND_ROTATION': 'BOND_ROTATION', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'QPARM': 'QPARM', 'HYDRONIUM_SHELL': 'HYDRONIUM_SHELL', 'HYDRONIUM_DISTANCE': 'HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_DISTANCE': 'ACID_HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_SHELL': 'ACID_HYDRONIUM_SHELL', 'RMSD': 'RMSD', 'XYZ_DIAG': 'XYZ_DIAG', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'U': 'U', 'WC': 'WC', 'HBP': 'HBP', 'RING_PUCKERING': 'RING_PUCKERING', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO'}
        self._repeated_subsections = {'PRINT': '_print53'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print53()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

