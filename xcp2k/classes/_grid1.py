from xcp2k.inputsection import InputSection


class _grid1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Backend = None
        self.Validate = None
        self.Apply_cutoff = None
        self.Queue_length = None
        self._name = "GRID"
        self._keywords = {'Backend': 'BACKEND', 'Validate': 'VALIDATE', 'Apply_cutoff': 'APPLY_CUTOFF', 'Queue_length': 'QUEUE_LENGTH'}

