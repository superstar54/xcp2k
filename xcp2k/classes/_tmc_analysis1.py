from xcp2k.inputsection import InputSection
from xcp2k.classes._charge1 import _charge1


class _tmc_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Restart = None
        self.Prefix_ana_files = None
        self.Density = None
        self.G_r = None
        self.Classical_dipole_moments = None
        self.Dipole_analysis = None
        self.Deviation = None
        self.CHARGE_list = []
        self._name = "TMC_ANALYSIS"
        self._keywords = {'Restart': 'RESTART', 'Prefix_ana_files': 'PREFIX_ANA_FILES', 'Density': 'DENSITY', 'G_r': 'G_R', 'Classical_dipole_moments': 'CLASSICAL_DIPOLE_MOMENTS', 'Dipole_analysis': 'DIPOLE_ANALYSIS', 'Deviation': 'DEVIATION'}
        self._repeated_subsections = {'CHARGE': '_charge1'}
        self._attributes = ['CHARGE_list']

    def CHARGE_add(self, section_parameters=None):
        new_section = _charge1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CHARGE_list.append(new_section)
        return new_section

