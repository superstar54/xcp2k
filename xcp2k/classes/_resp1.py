from xcp2k.inputsection import InputSection
from xcp2k.classes._constraint2 import _constraint2
from xcp2k.classes._restraint8 import _restraint8
from xcp2k.classes._sphere_sampling1 import _sphere_sampling1
from xcp2k.classes._slab_sampling1 import _slab_sampling1
from xcp2k.classes._print66 import _print66


class _resp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Stride = None
        self.Integer_total_charge = None
        self.Restrain_heavies_to_zero = None
        self.Restrain_heavies_strength = None
        self.Width = None
        self.Use_repeat_method = None
        self.CONSTRAINT_list = []
        self.RESTRAINT_list = []
        self.SPHERE_SAMPLING = _sphere_sampling1()
        self.SLAB_SAMPLING_list = []
        self.PRINT = _print66()
        self._name = "RESP"
        self._keywords = {'Stride': 'STRIDE', 'Integer_total_charge': 'INTEGER_TOTAL_CHARGE', 'Restrain_heavies_to_zero': 'RESTRAIN_HEAVIES_TO_ZERO', 'Restrain_heavies_strength': 'RESTRAIN_HEAVIES_STRENGTH', 'Width': 'WIDTH', 'Use_repeat_method': 'USE_REPEAT_METHOD'}
        self._subsections = {'SPHERE_SAMPLING': 'SPHERE_SAMPLING', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'CONSTRAINT': '_constraint2', 'RESTRAINT': '_restraint8', 'SLAB_SAMPLING': '_slab_sampling1'}
        self._attributes = ['CONSTRAINT_list', 'RESTRAINT_list', 'SLAB_SAMPLING_list']

    def CONSTRAINT_add(self, section_parameters=None):
        new_section = _constraint2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONSTRAINT_list.append(new_section)
        return new_section

    def RESTRAINT_add(self, section_parameters=None):
        new_section = _restraint8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RESTRAINT_list.append(new_section)
        return new_section

    def SLAB_SAMPLING_add(self, section_parameters=None):
        new_section = _slab_sampling1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SLAB_SAMPLING_list.append(new_section)
        return new_section

