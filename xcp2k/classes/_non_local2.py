from xcp2k.inputsection import InputSection


class _non_local2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Verbose_output = None
        self.Kernel_file_name = None
        self.Cutoff = None
        self.Parameters = None
        self._name = "NON_LOCAL"
        self._keywords = {'Type': 'TYPE', 'Verbose_output': 'VERBOSE_OUTPUT', 'Kernel_file_name': 'KERNEL_FILE_NAME', 'Cutoff': 'CUTOFF', 'Parameters': 'PARAMETERS'}

