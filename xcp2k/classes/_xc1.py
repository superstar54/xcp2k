from xcp2k.inputsection import InputSection
from xcp2k.classes._xc_grid1 import _xc_grid1
from xcp2k.classes._xc_functional1 import _xc_functional1
from xcp2k.classes._hf1 import _hf1
from xcp2k.classes._wf_correlation1 import _wf_correlation1
from xcp2k.classes._adiabatic_rescaling1 import _adiabatic_rescaling1
from xcp2k.classes._xc_potential1 import _xc_potential1
from xcp2k.classes._vdw_potential1 import _vdw_potential1
from xcp2k.classes._gcp_potential1 import _gcp_potential1


class _xc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Density_cutoff = None
        self.Gradient_cutoff = None
        self.Density_smooth_cutoff_range = None
        self.Tau_cutoff = None
        self.Functional_routine = None
        self.Num2nd_deriv_analytical = None
        self.Num3rd_deriv_analytical = None
        self.XC_GRID = _xc_grid1()
        self.XC_FUNCTIONAL = _xc_functional1()
        self.HF_list = []
        self.WF_CORRELATION_list = []
        self.ADIABATIC_RESCALING = _adiabatic_rescaling1()
        self.XC_POTENTIAL = _xc_potential1()
        self.VDW_POTENTIAL = _vdw_potential1()
        self.GCP_POTENTIAL = _gcp_potential1()
        self._name = "XC"
        self._keywords = {'Density_cutoff': 'DENSITY_CUTOFF', 'Gradient_cutoff': 'GRADIENT_CUTOFF', 'Density_smooth_cutoff_range': 'DENSITY_SMOOTH_CUTOFF_RANGE', 'Tau_cutoff': 'TAU_CUTOFF', 'Functional_routine': 'FUNCTIONAL_ROUTINE', 'Num2nd_deriv_analytical': '2ND_DERIV_ANALYTICAL', 'Num3rd_deriv_analytical': '3RD_DERIV_ANALYTICAL'}
        self._subsections = {'XC_GRID': 'XC_GRID', 'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'ADIABATIC_RESCALING': 'ADIABATIC_RESCALING', 'XC_POTENTIAL': 'XC_POTENTIAL', 'VDW_POTENTIAL': 'VDW_POTENTIAL', 'GCP_POTENTIAL': 'GCP_POTENTIAL'}
        self._repeated_subsections = {'HF': '_hf1', 'WF_CORRELATION': '_wf_correlation1'}
        self._attributes = ['HF_list', 'WF_CORRELATION_list']

    def HF_add(self, section_parameters=None):
        new_section = _hf1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section

    def WF_CORRELATION_add(self, section_parameters=None):
        new_section = _wf_correlation1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WF_CORRELATION_list.append(new_section)
        return new_section

