from xcp2k.inputsection import InputSection
from xcp2k.classes._distance2 import _distance2
from xcp2k.classes._angle3 import _angle3
from xcp2k.classes._torsion4 import _torsion4
from xcp2k.classes._coordination2 import _coordination2
from xcp2k.classes._population2 import _population2
from xcp2k.classes._gyration_radius2 import _gyration_radius2
from xcp2k.classes._distance_point_plane2 import _distance_point_plane2
from xcp2k.classes._angle_plane_plane2 import _angle_plane_plane2
from xcp2k.classes._bond_rotation2 import _bond_rotation2
from xcp2k.classes._distance_function2 import _distance_function2
from xcp2k.classes._qparm2 import _qparm2
from xcp2k.classes._hydronium_shell2 import _hydronium_shell2
from xcp2k.classes._hydronium_distance2 import _hydronium_distance2
from xcp2k.classes._acid_hydronium_distance2 import _acid_hydronium_distance2
from xcp2k.classes._acid_hydronium_shell2 import _acid_hydronium_shell2
from xcp2k.classes._rmsd2 import _rmsd2
from xcp2k.classes._xyz_diag2 import _xyz_diag2
from xcp2k.classes._xyz_outerdiag2 import _xyz_outerdiag2
from xcp2k.classes._u2 import _u2
from xcp2k.classes._wc2 import _wc2
from xcp2k.classes._hbp2 import _hbp2
from xcp2k.classes._ring_puckering2 import _ring_puckering2
from xcp2k.classes._conditioned_distance2 import _conditioned_distance2
from xcp2k.classes._print66 import _print66
from xcp2k.classes._colvar_func_info1 import _colvar_func_info1


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
        self.HYDRONIUM_SHELL = _hydronium_shell2()
        self.HYDRONIUM_DISTANCE = _hydronium_distance2()
        self.ACID_HYDRONIUM_DISTANCE = _acid_hydronium_distance2()
        self.ACID_HYDRONIUM_SHELL = _acid_hydronium_shell2()
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
        self._subsections = {'DISTANCE': 'DISTANCE', 'ANGLE': 'ANGLE', 'TORSION': 'TORSION', 'COORDINATION': 'COORDINATION', 'POPULATION': 'POPULATION', 'GYRATION_RADIUS': 'GYRATION_RADIUS', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'BOND_ROTATION': 'BOND_ROTATION', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'QPARM': 'QPARM', 'HYDRONIUM_SHELL': 'HYDRONIUM_SHELL', 'HYDRONIUM_DISTANCE': 'HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_DISTANCE': 'ACID_HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_SHELL': 'ACID_HYDRONIUM_SHELL', 'RMSD': 'RMSD', 'XYZ_DIAG': 'XYZ_DIAG', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'U': 'U', 'WC': 'WC', 'HBP': 'HBP', 'RING_PUCKERING': 'RING_PUCKERING', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO'}
        self._repeated_subsections = {'PRINT': '_print66'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print66()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

