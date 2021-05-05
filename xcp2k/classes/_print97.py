from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info61 import _program_run_info61
from xcp2k.classes._dos4 import _dos4
from xcp2k.classes._transmission1 import _transmission1


class _print97(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info61()
        self.DOS = _dos4()
        self.TRANSMISSION = _transmission1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'DOS': 'DOS', 'TRANSMISSION': 'TRANSMISSION'}

