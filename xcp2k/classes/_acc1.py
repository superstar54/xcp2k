from xcp2k.inputsection import InputSection


class _acc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Priority_buffers = None
        self.Posterior_buffers = None
        self.Priority_streams = None
        self.Posterior_streams = None
        self.Avoid_after_busy = None
        self.Min_flop_process = None
        self.Stack_sort = None
        self.Min_flop_sort = None
        self.Process_inhomogenous = None
        self.Binning_nbins = None
        self.Binning_binsize = None
        self._name = "ACC"
        self._keywords = {'Priority_buffers': 'PRIORITY_BUFFERS', 'Posterior_buffers': 'POSTERIOR_BUFFERS', 'Priority_streams': 'PRIORITY_STREAMS', 'Posterior_streams': 'POSTERIOR_STREAMS', 'Avoid_after_busy': 'AVOID_AFTER_BUSY', 'Min_flop_process': 'MIN_FLOP_PROCESS', 'Stack_sort': 'STACK_SORT', 'Min_flop_sort': 'MIN_FLOP_SORT', 'Process_inhomogenous': 'PROCESS_INHOMOGENOUS', 'Binning_nbins': 'BINNING_NBINS', 'Binning_binsize': 'BINNING_BINSIZE'}

