from xcp2k.inputsection import InputSection


class _worm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Centroid_drmax = None
        self.Staging_l = None
        self.Open_close_scale = None
        self.Allow_open = None
        self.Show_statistics = None
        self.Centroid_weight = None
        self.Staging_weight = None
        self.Open_close_weight = None
        self.Head_tail_weight = None
        self.Crawl_weight = None
        self.Crawl_repetition = None
        self.Swap_weight = None
        self._name = "WORM"
        self._keywords = {'Centroid_drmax': 'CENTROID_DRMAX', 'Staging_l': 'STAGING_L', 'Open_close_scale': 'OPEN_CLOSE_SCALE', 'Allow_open': 'ALLOW_OPEN', 'Show_statistics': 'SHOW_STATISTICS', 'Centroid_weight': 'CENTROID_WEIGHT', 'Staging_weight': 'STAGING_WEIGHT', 'Open_close_weight': 'OPEN_CLOSE_WEIGHT', 'Head_tail_weight': 'HEAD_TAIL_WEIGHT', 'Crawl_weight': 'CRAWL_WEIGHT', 'Crawl_repetition': 'CRAWL_REPETITION', 'Swap_weight': 'SWAP_WEIGHT'}

