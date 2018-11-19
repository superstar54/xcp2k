from xcp2k.inputsection import InputSection


class _bulk_region1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Molname = []
        self._name = "BULK_REGION"
        self._repeated_keywords = {'Molname': 'MOLNAME', 'List': 'LIST'}

