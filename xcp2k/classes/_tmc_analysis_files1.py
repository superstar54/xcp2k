from xcp2k.inputsection import InputSection
from xcp2k.classes._charge2 import _charge2


class _tmc_analysis_files1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Restart = None
        self.Prefix_ana_files = None
        self.Density = None
        self.G_r = None
        self.Classical_dipole_moments = None
        self.Dipole_analysis = None
        self.Deviation = None
        self.Nr_temperature = None
        self.Temperature = None
        self.Directories = None
        self.Force_env_file = None
        self.Position_file = None
        self.Cell_file = None
        self.Dipole_file = None
        self.Start_elem = None
        self.End_elem = None
        self.CHARGE_list = []
        self._name = "TMC_ANALYSIS_FILES"
        self._keywords = {'Restart': 'RESTART', 'Prefix_ana_files': 'PREFIX_ANA_FILES', 'Density': 'DENSITY', 'G_r': 'G_R', 'Classical_dipole_moments': 'CLASSICAL_DIPOLE_MOMENTS', 'Dipole_analysis': 'DIPOLE_ANALYSIS', 'Deviation': 'DEVIATION', 'Nr_temperature': 'NR_TEMPERATURE', 'Temperature': 'TEMPERATURE', 'Directories': 'DIRECTORIES', 'Force_env_file': 'FORCE_ENV_FILE', 'Position_file': 'POSITION_FILE', 'Cell_file': 'CELL_FILE', 'Dipole_file': 'DIPOLE_FILE', 'Start_elem': 'START_ELEM', 'End_elem': 'END_ELEM'}
        self._repeated_subsections = {'CHARGE': '_charge2'}
        self._attributes = ['CHARGE_list']

    def CHARGE_add(self, section_parameters=None):
        new_section = _charge2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CHARGE_list.append(new_section)
        return new_section

