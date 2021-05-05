from xcp2k.inputsection import InputSection
from xcp2k.classes._distance3 import _distance3
from xcp2k.classes._angle4 import _angle4
from xcp2k.classes._torsion5 import _torsion5
from xcp2k.classes._coordination3 import _coordination3
from xcp2k.classes._population3 import _population3
from xcp2k.classes._gyration_radius3 import _gyration_radius3
from xcp2k.classes._distance_point_plane3 import _distance_point_plane3
from xcp2k.classes._angle_plane_plane3 import _angle_plane_plane3
from xcp2k.classes._bond_rotation3 import _bond_rotation3
from xcp2k.classes._distance_function3 import _distance_function3
from xcp2k.classes._qparm3 import _qparm3
from xcp2k.classes._hydronium_shell3 import _hydronium_shell3
from xcp2k.classes._hydronium_distance3 import _hydronium_distance3
from xcp2k.classes._acid_hydronium_distance3 import _acid_hydronium_distance3
from xcp2k.classes._acid_hydronium_shell3 import _acid_hydronium_shell3
from xcp2k.classes._rmsd3 import _rmsd3
from xcp2k.classes._xyz_diag3 import _xyz_diag3
from xcp2k.classes._xyz_outerdiag3 import _xyz_outerdiag3
from xcp2k.classes._u3 import _u3
from xcp2k.classes._wc3 import _wc3
from xcp2k.classes._hbp3 import _hbp3
from xcp2k.classes._ring_puckering3 import _ring_puckering3
from xcp2k.classes._conditioned_distance3 import _conditioned_distance3
from xcp2k.classes._print67 import _print67
from xcp2k.classes._colvar_func_info2 import _colvar_func_info2


class _colvar3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DISTANCE = _distance3()
        self.ANGLE = _angle4()
        self.TORSION = _torsion5()
        self.COORDINATION = _coordination3()
        self.POPULATION = _population3()
        self.GYRATION_RADIUS = _gyration_radius3()
        self.DISTANCE_POINT_PLANE = _distance_point_plane3()
        self.ANGLE_PLANE_PLANE = _angle_plane_plane3()
        self.BOND_ROTATION = _bond_rotation3()
        self.DISTANCE_FUNCTION = _distance_function3()
        self.QPARM = _qparm3()
        self.HYDRONIUM_SHELL = _hydronium_shell3()
        self.HYDRONIUM_DISTANCE = _hydronium_distance3()
        self.ACID_HYDRONIUM_DISTANCE = _acid_hydronium_distance3()
        self.ACID_HYDRONIUM_SHELL = _acid_hydronium_shell3()
        self.RMSD = _rmsd3()
        self.XYZ_DIAG = _xyz_diag3()
        self.XYZ_OUTERDIAG = _xyz_outerdiag3()
        self.U = _u3()
        self.WC = _wc3()
        self.HBP = _hbp3()
        self.RING_PUCKERING = _ring_puckering3()
        self.CONDITIONED_DISTANCE = _conditioned_distance3()
        self.PRINT_list = []
        self.COLVAR_FUNC_INFO = _colvar_func_info2()
        self._name = "COLVAR"
        self._subsections = {'DISTANCE': 'DISTANCE', 'ANGLE': 'ANGLE', 'TORSION': 'TORSION', 'COORDINATION': 'COORDINATION', 'POPULATION': 'POPULATION', 'GYRATION_RADIUS': 'GYRATION_RADIUS', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'BOND_ROTATION': 'BOND_ROTATION', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'QPARM': 'QPARM', 'HYDRONIUM_SHELL': 'HYDRONIUM_SHELL', 'HYDRONIUM_DISTANCE': 'HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_DISTANCE': 'ACID_HYDRONIUM_DISTANCE', 'ACID_HYDRONIUM_SHELL': 'ACID_HYDRONIUM_SHELL', 'RMSD': 'RMSD', 'XYZ_DIAG': 'XYZ_DIAG', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'U': 'U', 'WC': 'WC', 'HBP': 'HBP', 'RING_PUCKERING': 'RING_PUCKERING', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO'}
        self._repeated_subsections = {'PRINT': '_print67'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print67()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

