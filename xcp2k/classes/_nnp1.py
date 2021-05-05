from xcp2k.inputsection import InputSection
from xcp2k.classes._bias1 import _bias1
from xcp2k.classes._model1 import _model1
from xcp2k.classes._print59 import _print59


class _nnp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nnp_input_file_name = None
        self.Scale_file_name = None
        self.BIAS = _bias1()
        self.MODEL_list = []
        self.PRINT = _print59()
        self._name = "NNP"
        self._keywords = {'Nnp_input_file_name': 'NNP_INPUT_FILE_NAME', 'Scale_file_name': 'SCALE_FILE_NAME'}
        self._subsections = {'BIAS': 'BIAS', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'MODEL': '_model1'}
        self._attributes = ['MODEL_list']

    def MODEL_add(self, section_parameters=None):
        new_section = _model1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MODEL_list.append(new_section)
        return new_section

