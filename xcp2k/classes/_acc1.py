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
        self.Min_flop_sort = None
        self.Process_inhomogenous = None
        self.Binning_nbins = None
        self.Binning_binsize = None
        self._name = "ACC"
        self._keywords = {'Posterior_buffers': 'POSTERIOR_BUFFERS', 'Priority_streams': 'PRIORITY_STREAMS', 'Priority_buffers': 'PRIORITY_BUFFERS', 'Binning_binsize': 'BINNING_BINSIZE', 'Process_inhomogenous': 'PROCESS_INHOMOGENOUS', 'Posterior_streams': 'POSTERIOR_STREAMS', 'Min_flop_process': 'MIN_FLOP_PROCESS', 'Avoid_after_busy': 'AVOID_AFTER_BUSY', 'Min_flop_sort': 'MIN_FLOP_SORT', 'Binning_nbins': 'BINNING_NBINS'}

