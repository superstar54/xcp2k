from xcp2k.inputsection import InputSection
from _dump_pdb1 import _dump_pdb1
from _dump_psf1 import _dump_psf1
from _exclude_vdw_list1 import _exclude_vdw_list1
from _exclude_ei_list1 import _exclude_ei_list1
from _center_coordinates1 import _center_coordinates1
from _generate1 import _generate1
from _mol_set1 import _mol_set1


class _topology1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Charge_occup = None
        self.Charge_beta = None
        self.Charge_extended = None
        self.Para_res = None
        self.Mol_check = None
        self.Use_g96_velocity = None
        self.Coord_file_name = None
        self.Coord_file_format = None
        self.Number_of_atoms = None
        self.Conn_file_name = None
        self.Conn_file_format = None
        self.Disable_exclusion_lists = None
        self.Exclude_vdw = None
        self.Exclude_ei = None
        self.Autogen_exclude_lists = None
        self.Multiple_unit_cell = None
        self.Memory_progression_factor = None
        self.DUMP_PDB = _dump_pdb1()
        self.DUMP_PSF = _dump_psf1()
        self.EXCLUDE_VDW_LIST = _exclude_vdw_list1()
        self.EXCLUDE_EI_LIST = _exclude_ei_list1()
        self.CENTER_COORDINATES = _center_coordinates1()
        self.GENERATE_list = []
        self.MOL_SET = _mol_set1()
        self._name = "TOPOLOGY"
        self._keywords = {'Mol_check': 'MOL_CHECK', 'Use_g96_velocity': 'USE_G96_VELOCITY', 'Charge_beta': 'CHARGE_BETA', 'Memory_progression_factor': 'MEMORY_PROGRESSION_FACTOR', 'Number_of_atoms': 'NUMBER_OF_ATOMS', 'Conn_file_name': 'CONN_FILE_NAME', 'Conn_file_format': 'CONN_FILE_FORMAT', 'Coord_file_format': 'COORD_FILE_FORMAT', 'Exclude_vdw': 'EXCLUDE_VDW', 'Autogen_exclude_lists': 'AUTOGEN_EXCLUDE_LISTS', 'Para_res': 'PARA_RES', 'Multiple_unit_cell': 'MULTIPLE_UNIT_CELL', 'Charge_occup': 'CHARGE_OCCUP', 'Coord_file_name': 'COORD_FILE_NAME', 'Charge_extended': 'CHARGE_EXTENDED', 'Disable_exclusion_lists': 'DISABLE_EXCLUSION_LISTS', 'Exclude_ei': 'EXCLUDE_EI'}
        self._subsections = {'EXCLUDE_EI_LIST': 'EXCLUDE_EI_LIST', 'CENTER_COORDINATES': 'CENTER_COORDINATES', 'DUMP_PSF': 'DUMP_PSF', 'EXCLUDE_VDW_LIST': 'EXCLUDE_VDW_LIST', 'MOL_SET': 'MOL_SET', 'DUMP_PDB': 'DUMP_PDB'}
        self._repeated_subsections = {'GENERATE': '_generate1'}
        self._aliases = {'Natoms': 'Number_of_atoms', 'Charge_b': 'Charge_beta', 'Conn_file': 'Conn_file_name', 'Connectivity': 'Conn_file_format', 'Charge_o': 'Charge_occup', 'Natom': 'Number_of_atoms', 'Coordinate': 'Coord_file_format', 'Coord_file': 'Coord_file_name'}
        self._attributes = ['GENERATE_list']

    def GENERATE_add(self, section_parameters=None):
        new_section = _generate1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GENERATE_list.append(new_section)
        return new_section


    @property
    def Charge_o(self):
        """
        See documentation for Charge_occup
        """
        return self.Charge_occup

    @property
    def Charge_b(self):
        """
        See documentation for Charge_beta
        """
        return self.Charge_beta

    @property
    def Coord_file(self):
        """
        See documentation for Coord_file_name
        """
        return self.Coord_file_name

    @property
    def Coordinate(self):
        """
        See documentation for Coord_file_format
        """
        return self.Coord_file_format

    @property
    def Natoms(self):
        """
        See documentation for Number_of_atoms
        """
        return self.Number_of_atoms

    @property
    def Natom(self):
        """
        See documentation for Number_of_atoms
        """
        return self.Number_of_atoms

    @property
    def Conn_file(self):
        """
        See documentation for Conn_file_name
        """
        return self.Conn_file_name

    @property
    def Connectivity(self):
        """
        See documentation for Conn_file_format
        """
        return self.Conn_file_format

    @Charge_o.setter
    def Charge_o(self, value):
        self.Charge_occup = value

    @Charge_b.setter
    def Charge_b(self, value):
        self.Charge_beta = value

    @Coord_file.setter
    def Coord_file(self, value):
        self.Coord_file_name = value

    @Coordinate.setter
    def Coordinate(self, value):
        self.Coord_file_format = value

    @Natoms.setter
    def Natoms(self, value):
        self.Number_of_atoms = value

    @Natom.setter
    def Natom(self, value):
        self.Number_of_atoms = value

    @Conn_file.setter
    def Conn_file(self, value):
        self.Conn_file_name = value

    @Connectivity.setter
    def Connectivity(self, value):
        self.Conn_file_format = value
