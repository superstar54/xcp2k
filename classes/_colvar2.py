from xcp2k.inputsection import InputSection
from _distance2 import _distance2
from _angle3 import _angle3
from _torsion4 import _torsion4
from _coordination2 import _coordination2
from _population2 import _population2
from _gyration_radius2 import _gyration_radius2
from _distance_point_plane2 import _distance_point_plane2
from _angle_plane_plane2 import _angle_plane_plane2
from _bond_rotation2 import _bond_rotation2
from _distance_function2 import _distance_function2
from _qparm2 import _qparm2
from _hydronium2 import _hydronium2
from _rmsd2 import _rmsd2
from _xyz_diag2 import _xyz_diag2
from _xyz_outerdiag2 import _xyz_outerdiag2
from _u2 import _u2
from _wc2 import _wc2
from _hbp2 import _hbp2
from _ring_puckering2 import _ring_puckering2
from _conditioned_distance2 import _conditioned_distance2
from _print42 import _print42
from _colvar_func_info1 import _colvar_func_info1


class _colvar2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DISTANCE = _distance2()
        self.ANGLE = _angle3()
        self.TORSION = _torsion4()
        self.COORDINATION = _coordination2()
        self.POPULATION = _population2()
        self.GYRATION_RADIUS = _gyration_radius2()
        self.DISTANCE_POINT_PLANE = _distance_point_plane2()
        self.ANGLE_PLANE_PLANE = _angle_plane_plane2()
        self.BOND_ROTATION = _bond_rotation2()
        self.DISTANCE_FUNCTION = _distance_function2()
        self.QPARM = _qparm2()
        self.HYDRONIUM = _hydronium2()
        self.RMSD = _rmsd2()
        self.XYZ_DIAG = _xyz_diag2()
        self.XYZ_OUTERDIAG = _xyz_outerdiag2()
        self.U = _u2()
        self.WC = _wc2()
        self.HBP = _hbp2()
        self.RING_PUCKERING = _ring_puckering2()
        self.CONDITIONED_DISTANCE = _conditioned_distance2()
        self.PRINT_list = []
        self.COLVAR_FUNC_INFO = _colvar_func_info1()
        self._name = "COLVAR"
        self._subsections = {'GYRATION_RADIUS': 'GYRATION_RADIUS', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO', 'ANGLE': 'ANGLE', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'RMSD': 'RMSD', 'DISTANCE': 'DISTANCE', 'HYDRONIUM': 'HYDRONIUM', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'RING_PUCKERING': 'RING_PUCKERING', 'U': 'U', 'BOND_ROTATION': 'BOND_ROTATION', 'QPARM': 'QPARM', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'XYZ_DIAG': 'XYZ_DIAG', 'TORSION': 'TORSION', 'HBP': 'HBP', 'COORDINATION': 'COORDINATION', 'WC': 'WC', 'POPULATION': 'POPULATION'}
        self._repeated_subsections = {'PRINT': '_print42'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print42()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

