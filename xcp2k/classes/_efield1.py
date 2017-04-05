from xcp2k.inputsection import InputSection
from _constant_env1 import _constant_env1
from _ramp_env1 import _ramp_env1
from _gaussian_env1 import _gaussian_env1


class _efield1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Intensity = None
        self.Polarisation = None
        self.Wavelength = None
        self.Phase = None
        self.Envelop = None
        self.CONSTANT_ENV_list = []
        self.RAMP_ENV_list = []
        self.GAUSSIAN_ENV_list = []
        self._name = "EFIELD"
        self._keywords = {'Phase': 'PHASE', 'Wavelength': 'WAVELENGTH', 'Intensity': 'INTENSITY', 'Envelop': 'ENVELOP', 'Polarisation': 'POLARISATION'}
        self._repeated_subsections = {'RAMP_ENV': '_ramp_env1', 'CONSTANT_ENV': '_constant_env1', 'GAUSSIAN_ENV': '_gaussian_env1'}
        self._attributes = ['CONSTANT_ENV_list', 'RAMP_ENV_list', 'GAUSSIAN_ENV_list']

    def RAMP_ENV_add(self, section_parameters=None):
        new_section = _ramp_env1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RAMP_ENV_list.append(new_section)
        return new_section

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

