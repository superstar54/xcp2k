from xcp2k.inputsection import InputSection
from xcp2k.classes._external_potential1 import _external_potential1
from xcp2k.classes._rescale_forces1 import _rescale_forces1
from xcp2k.classes._mixed1 import _mixed1
from xcp2k.classes._embed1 import _embed1
from xcp2k.classes._dft1 import _dft1
from xcp2k.classes._mm1 import _mm1
from xcp2k.classes._qmmm1 import _qmmm1
from xcp2k.classes._eip1 import _eip1
from xcp2k.classes._bsse1 import _bsse1
from xcp2k.classes._subsys1 import _subsys1
from xcp2k.classes._properties1 import _properties1
from xcp2k.classes._print68 import _print68


class _force_eval3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Stress_tensor = None
        self.Embed = None
        self.EXTERNAL_POTENTIAL_list = []
        self.RESCALE_FORCES = _rescale_forces1()
        self.MIXED = _mixed1()
        self.EMBED = _embed1()
        self.DFT = _dft1()
        self.MM = _mm1()
        self.QMMM = _qmmm1()
        self.EIP = _eip1()
        self.BSSE = _bsse1()
        self.SUBSYS = _subsys1()
        self.PROPERTIES = _properties1()
        self.PRINT = _print68()
        self._name = "FORCE_EVAL"
        self._keywords = {'Method': 'METHOD', 'Stress_tensor': 'STRESS_TENSOR', 'Embed': 'EMBED'}
        self._subsections = {'RESCALE_FORCES': 'RESCALE_FORCES', 'MIXED': 'MIXED', 'EMBED': 'EMBED', 'DFT': 'DFT', 'MM': 'MM', 'QMMM': 'QMMM', 'EIP': 'EIP', 'BSSE': 'BSSE', 'SUBSYS': 'SUBSYS', 'PROPERTIES': 'PROPERTIES', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'EXTERNAL_POTENTIAL': '_external_potential1'}
        self._attributes = ['EXTERNAL_POTENTIAL_list']

    def EXTERNAL_POTENTIAL_add(self, section_parameters=None):
        new_section = _external_potential1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.EXTERNAL_POTENTIAL_list.append(new_section)
        return new_section

