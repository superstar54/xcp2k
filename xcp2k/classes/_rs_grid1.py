from xcp2k.inputsection import InputSection


class _rs_grid1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Distribution_type = None
        self.Distribution_layout = None
        self.Max_distributed_level = None
        self.Lock_distribution = None
        self.Memory_factor = None
        self.Halo_reduction_factor = None
        self._name = "RS_GRID"
        self._keywords = {'Halo_reduction_factor': 'HALO_REDUCTION_FACTOR', 'Max_distributed_level': 'MAX_DISTRIBUTED_LEVEL', 'Lock_distribution': 'LOCK_DISTRIBUTION', 'Distribution_type': 'DISTRIBUTION_TYPE', 'Memory_factor': 'MEMORY_FACTOR', 'Distribution_layout': 'DISTRIBUTION_LAYOUT'}

