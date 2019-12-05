from xcp2k.inputsection import InputSection
from xcp2k.classes._nablavks_cubes1 import _nablavks_cubes1
from xcp2k.classes._g_tensor1 import _g_tensor1
from xcp2k.classes._response_function_cubes3 import _response_function_cubes3


class _print62(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NABLAVKS_CUBES = _nablavks_cubes1()
        self.G_TENSOR = _g_tensor1()
        self.RESPONSE_FUNCTION_CUBES = _response_function_cubes3()
        self._name = "PRINT"
        self._subsections = {'NABLAVKS_CUBES': 'NABLAVKS_CUBES', 'G_TENSOR': 'G_TENSOR', 'RESPONSE_FUNCTION_CUBES': 'RESPONSE_FUNCTION_CUBES'}

