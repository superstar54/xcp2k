from xcp2k.inputsection import InputSection


class _memory14(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_storage_scaling = None
        self.Max_memory = None
        self.Storage_location = None
        self.Max_disk_space = None
        self.Treat_forces_in_core = None
        self._name = "MEMORY"
        self._keywords = {'Eps_storage_scaling': 'EPS_STORAGE_SCALING', 'Max_memory': 'MAX_MEMORY', 'Storage_location': 'STORAGE_LOCATION', 'Max_disk_space': 'MAX_DISK_SPACE', 'Treat_forces_in_core': 'TREAT_FORCES_IN_CORE'}
        self._aliases = {'Eps_storage': 'Eps_storage_scaling'}


    @property
    def Eps_storage(self):
        """
        See documentation for Eps_storage_scaling
        """
        return self.Eps_storage_scaling

    @Eps_storage.setter
    def Eps_storage(self, value):
        self.Eps_storage_scaling = value
