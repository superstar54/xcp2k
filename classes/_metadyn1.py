from xcp2k.inputsection import InputSection
from _metavar1 import _metavar1
from _multiple_walkers1 import _multiple_walkers1
from _print13 import _print13
from _spawned_hills_pos1 import _spawned_hills_pos1
from _spawned_hills_scale1 import _spawned_hills_scale1
from _spawned_hills_height1 import _spawned_hills_height1
from _spawned_hills_invdt1 import _spawned_hills_invdt1
from _ext_lagrange_ss01 import _ext_lagrange_ss01
from _ext_lagrange_vvp1 import _ext_lagrange_vvp1
from _ext_lagrange_ss1 import _ext_lagrange_ss1
from _ext_lagrange_fs1 import _ext_lagrange_fs1


class _metadyn1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Use_plumed = None
        self.Plumed_input_file = None
        self.Min_nt_hills = None
        self.Nt_hills = None
        self.Temperature = None
        self.Min_disp = None
        self.Old_hill_number = None
        self.Old_hill_step = None
        self.Hill_tail_cutoff = None
        self.P_exponent = None
        self.Q_exponent = None
        self.Slow_growth = None
        self.Temp_tol = None
        self.Langevin = None
        self.Ww = None
        self.Do_hills = None
        self.Well_tempered = None
        self.Delta_t = None
        self.Wtgamma = None
        self.Lagrange = None
        self.Step_start_val = None
        self.Nhills_start_val = None
        self.Colvar_avg_temperature_restart = None
        self.Tamcsteps = None
        self.Timestep = None
        self.METAVAR_list = []
        self.MULTIPLE_WALKERS = _multiple_walkers1()
        self.PRINT_list = []
        self.SPAWNED_HILLS_POS = _spawned_hills_pos1()
        self.SPAWNED_HILLS_SCALE = _spawned_hills_scale1()
        self.SPAWNED_HILLS_HEIGHT = _spawned_hills_height1()
        self.SPAWNED_HILLS_INVDT = _spawned_hills_invdt1()
        self.EXT_LAGRANGE_SS0 = _ext_lagrange_ss01()
        self.EXT_LAGRANGE_VVP = _ext_lagrange_vvp1()
        self.EXT_LAGRANGE_SS = _ext_lagrange_ss1()
        self.EXT_LAGRANGE_FS = _ext_lagrange_fs1()
        self._name = "METADYN"
        self._keywords = {'Well_tempered': 'WELL_TEMPERED', 'Temperature': 'TEMPERATURE', 'Langevin': 'LANGEVIN', 'Wtgamma': 'WTGAMMA', 'Temp_tol': 'TEMP_TOL', 'Min_nt_hills': 'MIN_NT_HILLS', 'Nhills_start_val': 'NHILLS_START_VAL', 'Q_exponent': 'Q_EXPONENT', 'Old_hill_step': 'OLD_HILL_STEP', 'Plumed_input_file': 'PLUMED_INPUT_FILE', 'Tamcsteps': 'TAMCSTEPS', 'Ww': 'WW', 'Old_hill_number': 'OLD_HILL_NUMBER', 'Use_plumed': 'USE_PLUMED', 'Slow_growth': 'SLOW_GROWTH', 'Nt_hills': 'NT_HILLS', 'Colvar_avg_temperature_restart': 'COLVAR_AVG_TEMPERATURE_RESTART', 'P_exponent': 'P_EXPONENT', 'Hill_tail_cutoff': 'HILL_TAIL_CUTOFF', 'Do_hills': 'DO_HILLS', 'Step_start_val': 'STEP_START_VAL', 'Min_disp': 'MIN_DISP', 'Delta_t': 'DELTA_T', 'Timestep': 'TIMESTEP', 'Lagrange': 'LAGRANGE'}
        self._subsections = {'EXT_LAGRANGE_FS': 'EXT_LAGRANGE_FS', 'MULTIPLE_WALKERS': 'MULTIPLE_WALKERS', 'EXT_LAGRANGE_VVP': 'EXT_LAGRANGE_VVP', 'EXT_LAGRANGE_SS0': 'EXT_LAGRANGE_SS0', 'SPAWNED_HILLS_INVDT': 'SPAWNED_HILLS_INVDT', 'SPAWNED_HILLS_POS': 'SPAWNED_HILLS_POS', 'SPAWNED_HILLS_SCALE': 'SPAWNED_HILLS_SCALE', 'EXT_LAGRANGE_SS': 'EXT_LAGRANGE_SS', 'SPAWNED_HILLS_HEIGHT': 'SPAWNED_HILLS_HEIGHT'}
        self._repeated_subsections = {'PRINT': '_print13', 'METAVAR': '_metavar1'}
        self._attributes = ['METAVAR_list', 'PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print13()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

    def METAVAR_add(self, section_parameters=None):
        new_section = _metavar1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.METAVAR_list.append(new_section)
        return new_section

