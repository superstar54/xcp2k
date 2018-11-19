from xcp2k.inputsection import InputSection
from _xc_grid6 import _xc_grid6
from _xc_functional6 import _xc_functional6
from _hf11 import _hf11
from _wf_correlation6 import _wf_correlation6
from _adiabatic_rescaling6 import _adiabatic_rescaling6
from _xc_potential6 import _xc_potential6
from _vdw_potential6 import _vdw_potential6


class _xc6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Density_cutoff = None
        self.Gradient_cutoff = None
        self.Density_smooth_cutoff_range = None
        self.Tau_cutoff = None
        self.Functional_routine = None
        self.XC_GRID = _xc_grid6()
        self.XC_FUNCTIONAL = _xc_functional6()
        self.HF_list = []
        self.WF_CORRELATION_list = []
        self.ADIABATIC_RESCALING = _adiabatic_rescaling6()
        self.XC_POTENTIAL = _xc_potential6()
        self.VDW_POTENTIAL = _vdw_potential6()
        self._name = "XC"
        self._keywords = {'Tau_cutoff': 'TAU_CUTOFF', 'Functional_routine': 'FUNCTIONAL_ROUTINE', 'Density_smooth_cutoff_range': 'DENSITY_SMOOTH_CUTOFF_RANGE', 'Density_cutoff': 'DENSITY_CUTOFF', 'Gradient_cutoff': 'GRADIENT_CUTOFF'}
        self._subsections = {'XC_POTENTIAL': 'XC_POTENTIAL', 'XC_GRID': 'XC_GRID', 'ADIABATIC_RESCALING': 'ADIABATIC_RESCALING', 'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'VDW_POTENTIAL': 'VDW_POTENTIAL'}
        self._repeated_subsections = {'WF_CORRELATION': '_wf_correlation6', 'HF': '_hf11'}
        self._attributes = ['HF_list', 'WF_CORRELATION_list']

    def WF_CORRELATION_add(self, section_parameters=None):
        new_section = _wf_correlation6()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WF_CORRELATION_list.append(new_section)
        return new_section

    def HF_add(self, section_parameters=None):
        new_section = _hf11()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section

