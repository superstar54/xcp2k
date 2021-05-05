from xcp2k.inputsection import InputSection
from xcp2k.classes._outer_scf2 import _outer_scf2
from xcp2k.classes._becke_constraint1 import _becke_constraint1
from xcp2k.classes._hirshfeld_constraint1 import _hirshfeld_constraint1
from xcp2k.classes._program_run_info20 import _program_run_info20
from xcp2k.classes._atom_group1 import _atom_group1
from xcp2k.classes._dummy_atoms1 import _dummy_atoms1


class _cdft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type_of_constraint = None
        self.Strength = None
        self.Target = None
        self.Atomic_charges = None
        self.Fragment_a_file_name = None
        self.Fragment_b_file_name = None
        self.Fragment_a_spin_file = None
        self.Fragment_b_spin_file = None
        self.Flip_fragment_a = None
        self.Flip_fragment_b = None
        self.Reuse_precond = None
        self.Precond_freq = None
        self.Max_reuse = None
        self.Purge_history = None
        self.Purge_freq = None
        self.Purge_offset = None
        self.Counter = None
        self.OUTER_SCF = _outer_scf2()
        self.BECKE_CONSTRAINT = _becke_constraint1()
        self.HIRSHFELD_CONSTRAINT = _hirshfeld_constraint1()
        self.PROGRAM_RUN_INFO = _program_run_info20()
        self.ATOM_GROUP_list = []
        self.DUMMY_ATOMS_list = []
        self._name = "CDFT"
        self._keywords = {'Type_of_constraint': 'TYPE_OF_CONSTRAINT', 'Strength': 'STRENGTH', 'Target': 'TARGET', 'Atomic_charges': 'ATOMIC_CHARGES', 'Fragment_a_file_name': 'FRAGMENT_A_FILE_NAME', 'Fragment_b_file_name': 'FRAGMENT_B_FILE_NAME', 'Fragment_a_spin_file': 'FRAGMENT_A_SPIN_FILE', 'Fragment_b_spin_file': 'FRAGMENT_B_SPIN_FILE', 'Flip_fragment_a': 'FLIP_FRAGMENT_A', 'Flip_fragment_b': 'FLIP_FRAGMENT_B', 'Reuse_precond': 'REUSE_PRECOND', 'Precond_freq': 'PRECOND_FREQ', 'Max_reuse': 'MAX_REUSE', 'Purge_history': 'PURGE_HISTORY', 'Purge_freq': 'PURGE_FREQ', 'Purge_offset': 'PURGE_OFFSET', 'Counter': 'COUNTER'}
        self._subsections = {'OUTER_SCF': 'OUTER_SCF', 'BECKE_CONSTRAINT': 'BECKE_CONSTRAINT', 'HIRSHFELD_CONSTRAINT': 'HIRSHFELD_CONSTRAINT', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}
        self._repeated_subsections = {'ATOM_GROUP': '_atom_group1', 'DUMMY_ATOMS': '_dummy_atoms1'}
        self._aliases = {'Fragment_a_file': 'Fragment_a_file_name', 'Fragment_b_file': 'Fragment_b_file_name', 'Fragment_a_spin_file_name': 'Fragment_a_spin_file', 'Fragment_b_spin_file_name': 'Fragment_b_spin_file'}
        self._attributes = ['ATOM_GROUP_list', 'DUMMY_ATOMS_list']

    def ATOM_GROUP_add(self, section_parameters=None):
        new_section = _atom_group1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.ATOM_GROUP_list.append(new_section)
        return new_section

    def DUMMY_ATOMS_add(self, section_parameters=None):
        new_section = _dummy_atoms1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DUMMY_ATOMS_list.append(new_section)
        return new_section


    @property
    def Fragment_a_file(self):
        """
        See documentation for Fragment_a_file_name
        """
        return self.Fragment_a_file_name

    @property
    def Fragment_b_file(self):
        """
        See documentation for Fragment_b_file_name
        """
        return self.Fragment_b_file_name

    @property
    def Fragment_a_spin_file_name(self):
        """
        See documentation for Fragment_a_spin_file
        """
        return self.Fragment_a_spin_file

    @property
    def Fragment_b_spin_file_name(self):
        """
        See documentation for Fragment_b_spin_file
        """
        return self.Fragment_b_spin_file

    @Fragment_a_file.setter
    def Fragment_a_file(self, value):
        self.Fragment_a_file_name = value

    @Fragment_b_file.setter
    def Fragment_b_file(self, value):
        self.Fragment_b_file_name = value

    @Fragment_a_spin_file_name.setter
    def Fragment_a_spin_file_name(self, value):
        self.Fragment_a_spin_file = value

    @Fragment_b_spin_file_name.setter
    def Fragment_b_spin_file_name(self, value):
        self.Fragment_b_spin_file = value
