from xcp2k.inputsection import InputSection


class _external_density1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_density = None
        self.Lambda = None
        self.Zmp_constraint = None
        self.Fermi_amaldi = None
        self._name = "EXTERNAL_DENSITY"
        self._keywords = {'Fermi_amaldi': 'FERMI_AMALDI', 'Zmp_constraint': 'ZMP_CONSTRAINT', 'File_density': 'FILE_DENSITY', 'Lambda': 'LAMBDA'}

