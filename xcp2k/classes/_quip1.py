from xcp2k.inputsection import InputSection


class _quip1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Parm_file_name = None
        self.Init_args = None
        self.Calc_args = None
        self._name = "QUIP"
        self._keywords = {'Init_args': 'INIT_ARGS', 'Calc_args': 'CALC_ARGS', 'Parm_file_name': 'PARM_FILE_NAME', 'Atoms': 'ATOMS'}
        self._aliases = {'Parmfile': 'Parm_file_name'}


    @property
    def Parmfile(self):
        """
        See documentation for Parm_file_name
        """
        return self.Parm_file_name

    @Parmfile.setter
    def Parmfile(self, value):
        self.Parm_file_name = value
