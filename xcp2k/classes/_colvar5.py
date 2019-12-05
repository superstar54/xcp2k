from xcp2k.inputsection import InputSection
from xcp2k.classes._distance1 import _distance1
from xcp2k.classes._angle2 import _angle2
from xcp2k.classes._torsion3 import _torsion3
from xcp2k.classes._coordination1 import _coordination1
from xcp2k.classes._population1 import _population1
from xcp2k.classes._gyration_radius1 import _gyration_radius1
from xcp2k.classes._distance_point_plane1 import _distance_point_plane1
from xcp2k.classes._angle_plane_plane1 import _angle_plane_plane1
from xcp2k.classes._bond_rotation1 import _bond_rotation1
from xcp2k.classes._distance_function1 import _distance_function1
from xcp2k.classes._qparm1 import _qparm1
from xcp2k.classes._hydronium_shell1 import _hydronium_shell1
from xcp2k.classes._hydronium_distance1 import _hydronium_distance1
from xcp2k.classes._acid_hydronium_distance1 import _acid_hydronium_distance1
from xcp2k.classes._acid_hydronium_shell1 import _acid_hydronium_shell1
from xcp2k.classes._rmsd1 import _rmsd1
from xcp2k.classes._xyz_diag1 import _xyz_diag1
from xcp2k.classes._xyz_outerdiag1 import _xyz_outerdiag1
from xcp2k.classes._u1 import _u1
from xcp2k.classes._wc1 import _wc1
from xcp2k.classes._hbp1 import _hbp1
from xcp2k.classes._ring_puckering1 import _ring_puckering1
from xcp2k.classes._conditioned_distance1 import _conditioned_distance1
from xcp2k.classes._reaction_path1 import _reaction_path1
from xcp2k.classes._distance_from_path1 import _distance_from_path1
from xcp2k.classes._combine_colvar1 import _combine_colvar1
from xcp2k.classes._print54 import _print54
from xcp2k.classes._colvar_func_info4 import _colvar_func_info4


class _colvar5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DISTANCE = _distance1()
        self.ANGLE = _angle2()
        self.TORSION = _torsion3()
        self.COORDINATION = _coordination1()
        self.POPULATION = _population1()
        self.GYRATION_RADIUS = _gyration_radius1()
        self.DISTANCE_POINT_PLANE = _distance_point_plane1()
        self.ANGLE_PLANE_PLANE = _angle_plane_plane1()
        self.BOND_ROTATION = _bond_rotation1()
        self.DISTANCE_FUNCTION = _distance_function1()
        self.QPARM = _qparm1()
        self.HYDRONIUM_SHELL = _hydronium_shell1()
        self.HYDRONIUM_DISTANCE = _hydronium_distance1()
        self.ACID_HYDRONIUM_DISTANCE = _acid_hydronium_distance1()
        self.ACID_HYDRONIUM_SHELL = _acid_hydronium_shell1()
        self.RMSD = _rmsd1()
        self.XYZ_DIAG = _xyz_diag1()
        self.XYZ_OUTERDIAG = _xyz_outerdiag1()
        self.U = _u1()
        self.WC = _wc1()
        self.HBP = _hbp1()
        self.RING_PUCKERING = _ring_puckering1()
        self.CONDITIONED_DISTANCE = _conditioned_distance1()
        self.REACTION_PATH = _reaction_path1()
        self.DISTANCE_FROM_PATH = _distance_from_path1()
        self.COMBINE_COLVAR = _combine_colvar1()
        self.PRINT_list = []
        self.COLVAR_FUNC_INFO = _colvar_func_info4()
        self._name = "COLVAR"
        self._subsections = {'DISTANCE': 'DISTANCE', 'ANGLE': 'ANGLE', 'TORSION': 'TORSION', 'COORDINATION': 'COORDINATION', 'POPULATION': 'POPULATION', 'GYRATION_RADIUS': 'GYRATION_RADIUS', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'BOND_ROTATION': 'BOND_ROTATION', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'QPARM': 'QPARM', 'HYDRONIUM_SHELL': 'HYDRONIUM_SHELL', 'HYDRONIUM_DISTANCE': 'HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_DISTANCE': 'ACID_HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_SHELL': 'ACID_HYDRONIUM_SHELL', 'RMSD': 'RMSD', 'XYZ_DIAG': 'XYZ_DIAG', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'U': 'U', 'WC': 'WC', 'HBP': 'HBP', 'RING_PUCKERING': 'RING_PUCKERING', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'REACTION_PATH': 'REACTION_PATH', 'DISTANCE_FROM_PATH': 'DISTANCE_FROM_PATH', 'COMBINE_COLVAR': 'COMBINE_COLVAR', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO'}
        self._repeated_subsections = {'PRINT': '_print54'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print54()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

