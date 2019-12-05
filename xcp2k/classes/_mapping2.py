from xcp2k.inputsection import InputSection
from xcp2k.classes._force_eval_embed1 import _force_eval_embed1
from xcp2k.classes._force_eval2 import _force_eval2


class _mapping2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.FORCE_EVAL_EMBED_list = []
        self.FORCE_EVAL_list = []
        self._name = "MAPPING"
        self._repeated_subsections = {'FORCE_EVAL_EMBED': '_force_eval_embed1', 'FORCE_EVAL': '_force_eval2'}
        self._attributes = ['FORCE_EVAL_EMBED_list', 'FORCE_EVAL_list']

    def FORCE_EVAL_EMBED_add(self, section_parameters=None):
        new_section = _force_eval_embed1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_EVAL_EMBED_list.append(new_section)
        return new_section

    def FORCE_EVAL_add(self, section_parameters=None):
        new_section = _force_eval2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_EVAL_list.append(new_section)
        return new_section

