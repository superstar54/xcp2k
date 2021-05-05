from xcp2k.inputsection import InputSection
from xcp2k.classes._bulk_region1 import _bulk_region1
from xcp2k.classes._screening_region1 import _screening_region1
from xcp2k.classes._print96 import _print96


class _contact2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Force_eval_section = None
        self.Electric_potential = None
        self.Fermi_level = None
        self.Refine_fermi_level = None
        self.Temperature = None
        self.BULK_REGION = _bulk_region1()
        self.SCREENING_REGION = _screening_region1()
        self.PRINT = _print96()
        self._name = "CONTACT"
        self._keywords = {'Force_eval_section': 'FORCE_EVAL_SECTION', 'Electric_potential': 'ELECTRIC_POTENTIAL', 'Fermi_level': 'FERMI_LEVEL', 'Refine_fermi_level': 'REFINE_FERMI_LEVEL', 'Temperature': 'TEMPERATURE'}
        self._subsections = {'BULK_REGION': 'BULK_REGION', 'SCREENING_REGION': 'SCREENING_REGION', 'PRINT': 'PRINT'}

