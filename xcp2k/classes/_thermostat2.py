from xcp2k.inputsection import InputSection
from xcp2k.classes._define_region1 import _define_region1
from xcp2k.classes._nose2 import _nose2
from xcp2k.classes._csvr2 import _csvr2
from xcp2k.classes._gle2 import _gle2
from xcp2k.classes._ad_langevin2 import _ad_langevin2
from xcp2k.classes._print8 import _print8


class _thermostat2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Region = None
        self.DEFINE_REGION_list = []
        self.NOSE = _nose2()
        self.CSVR = _csvr2()
        self.GLE = _gle2()
        self.AD_LANGEVIN = _ad_langevin2()
        self.PRINT = _print8()
        self._name = "THERMOSTAT"
        self._keywords = {'Type': 'TYPE', 'Region': 'REGION'}
        self._subsections = {'NOSE': 'NOSE', 'CSVR': 'CSVR', 'GLE': 'GLE', 'AD_LANGEVIN': 'AD_LANGEVIN', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'DEFINE_REGION': '_define_region1'}
        self._attributes = ['DEFINE_REGION_list']

    def DEFINE_REGION_add(self, section_parameters=None):
        new_section = _define_region1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DEFINE_REGION_list.append(new_section)
        return new_section

