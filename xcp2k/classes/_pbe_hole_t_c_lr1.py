from xcp2k.inputsection import InputSection


class _pbe_hole_t_c_lr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Cutoff_radius = None
        self._name = "PBE_HOLE_T_C_LR"
        self._keywords = {'Scale_x': 'SCALE_X', 'Cutoff_radius': 'CUTOFF_RADIUS'}
        self._attributes = ['Section_parameters']

