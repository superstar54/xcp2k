from xcp2k.inputsection import InputSection


class _define_region2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Molname = []
        self.Segname = self.Molname
        self.Mm_subsys = None
        self.Qm_subsys = None
        self._name = "DEFINE_REGION"
        self._keywords = {'Qm_subsys': 'QM_SUBSYS', 'Mm_subsys': 'MM_SUBSYS'}
        self._repeated_keywords = {'Molname': 'MOLNAME', 'List': 'LIST'}
        self._aliases = {'Protein': 'Mm_subsys'}
        self._repeated_aliases = {'Segname': 'Molname'}


    @property
    def Protein(self):
        """
        See documentation for Mm_subsys
        """
        return self.Mm_subsys

    @Protein.setter
    def Protein(self, value):
        self.Mm_subsys = value
