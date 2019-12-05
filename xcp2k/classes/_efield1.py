from xcp2k.inputsection import InputSection
from xcp2k.classes._constant_env1 import _constant_env1
from xcp2k.classes._gaussian_env1 import _gaussian_env1
from xcp2k.classes._ramp_env1 import _ramp_env1
from xcp2k.classes._custom_env1 import _custom_env1


class _efield1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Intensity = None
        self.Polarisation = None
        self.Wavelength = None
        self.Phase = None
        self.Envelop = None
        self.CONSTANT_ENV_list = []
        self.GAUSSIAN_ENV_list = []
        self.RAMP_ENV_list = []
        self.CUSTOM_ENV_list = []
        self._name = "EFIELD"
        self._keywords = {'Intensity': 'INTENSITY', 'Polarisation': 'POLARISATION', 'Wavelength': 'WAVELENGTH', 'Phase': 'PHASE', 'Envelop': 'ENVELOP'}
        self._repeated_subsections = {'CONSTANT_ENV': '_constant_env1', 'GAUSSIAN_ENV': '_gaussian_env1', 'RAMP_ENV': '_ramp_env1', 'CUSTOM_ENV': '_custom_env1'}
        self._attributes = ['CONSTANT_ENV_list', 'GAUSSIAN_ENV_list', 'RAMP_ENV_list', 'CUSTOM_ENV_list']

    def CONSTANT_ENV_add(self, section_parameters=None):
        new_section = _constant_env1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONSTANT_ENV_list.append(new_section)
        return new_section

    def GAUSSIAN_ENV_add(self, section_parameters=None):
        new_section = _gaussian_env1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GAUSSIAN_ENV_list.append(new_section)
        return new_section

    def RAMP_ENV_add(self, section_parameters=None):
        new_section = _ramp_env1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RAMP_ENV_list.append(new_section)
        return new_section

    def CUSTOM_ENV_add(self, section_parameters=None):
        new_section = _custom_env1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CUSTOM_ENV_list.append(new_section)
        return new_section

