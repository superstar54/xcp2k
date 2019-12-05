from xcp2k.inputsection import InputSection
from xcp2k.classes._move_type1 import _move_type1
from xcp2k.classes._nmc_moves1 import _nmc_moves1
from xcp2k.classes._tmc_analysis1 import _tmc_analysis1
from xcp2k.classes._tmc_analysis_files1 import _tmc_analysis_files1


class _tmc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Group_energy_size = None
        self.Group_energy_nr = None
        self.Group_cc_size = None
        self.Group_anlysis_nr = None
        self.Num_mc_elem = None
        self.Rnd_deterministic = None
        self.Task_type = None
        self.Nr_temperature = None
        self.Temperature = None
        self.Num_mv_elem_in_cell = None
        self.Sub_box = None
        self.Pressure = None
        self.Volume_isotropic = None
        self.Move_center_of_mass = None
        self.Esimate_acc_prob = None
        self.Speculative_canceling = None
        self.Use_scf_energy_info = None
        self.Result_list_in_memory = None
        self.Info_out_step_size = None
        self.Restart_in = None
        self.Restart_out = None
        self.Energy_file_name = None
        self.Print_only_acc = None
        self.Print_coords = None
        self.Print_forces = None
        self.Print_dipole = None
        self.Print_cell = None
        self.Print_energies = None
        self.Dot_tree = None
        self.All_conf_file_name = None
        self.Print_test_output = None
        self.MOVE_TYPE_list = []
        self.NMC_MOVES_list = []
        self.TMC_ANALYSIS = _tmc_analysis1()
        self.TMC_ANALYSIS_FILES = _tmc_analysis_files1()
        self._name = "TMC"
        self._keywords = {'Group_energy_size': 'GROUP_ENERGY_SIZE', 'Group_energy_nr': 'GROUP_ENERGY_NR', 'Group_cc_size': 'GROUP_CC_SIZE', 'Group_anlysis_nr': 'GROUP_ANLYSIS_NR', 'Num_mc_elem': 'NUM_MC_ELEM', 'Rnd_deterministic': 'RND_DETERMINISTIC', 'Task_type': 'TASK_TYPE', 'Nr_temperature': 'NR_TEMPERATURE', 'Temperature': 'TEMPERATURE', 'Num_mv_elem_in_cell': 'NUM_MV_ELEM_IN_CELL', 'Sub_box': 'SUB_BOX', 'Pressure': 'PRESSURE', 'Volume_isotropic': 'VOLUME_ISOTROPIC', 'Move_center_of_mass': 'MOVE_CENTER_OF_MASS', 'Esimate_acc_prob': 'ESIMATE_ACC_PROB', 'Speculative_canceling': 'SPECULATIVE_CANCELING', 'Use_scf_energy_info': 'USE_SCF_ENERGY_INFO', 'Result_list_in_memory': 'RESULT_LIST_IN_MEMORY', 'Info_out_step_size': 'INFO_OUT_STEP_SIZE', 'Restart_in': 'RESTART_IN', 'Restart_out': 'RESTART_OUT', 'Energy_file_name': 'ENERGY_FILE_NAME', 'Print_only_acc': 'PRINT_ONLY_ACC', 'Print_coords': 'PRINT_COORDS', 'Print_forces': 'PRINT_FORCES', 'Print_dipole': 'PRINT_DIPOLE', 'Print_cell': 'PRINT_CELL', 'Print_energies': 'PRINT_ENERGIES', 'Dot_tree': 'DOT_TREE', 'All_conf_file_name': 'ALL_CONF_FILE_NAME', 'Print_test_output': 'PRINT_TEST_OUTPUT'}
        self._subsections = {'TMC_ANALYSIS': 'TMC_ANALYSIS', 'TMC_ANALYSIS_FILES': 'TMC_ANALYSIS_FILES'}
        self._repeated_subsections = {'MOVE_TYPE': '_move_type1', 'NMC_MOVES': '_nmc_moves1'}
        self._attributes = ['MOVE_TYPE_list', 'NMC_MOVES_list']

    def MOVE_TYPE_add(self, section_parameters=None):
        new_section = _move_type1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MOVE_TYPE_list.append(new_section)
        return new_section

    def NMC_MOVES_add(self, section_parameters=None):
        new_section = _nmc_moves1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.NMC_MOVES_list.append(new_section)
        return new_section

