from xcp2k.inputsection import InputSection


class _sphere_sampling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.X_low = None
        self.X_hi = None
        self.Y_low = None
        self.Y_hi = None
        self.Z_low = None
        self.Z_hi = None
        self.Auto_vdw_radii_table = None
        self.Auto_rmax_scale = None
        self.Auto_rmin_scale = None
        self.Rmax = None
        self.Rmin = None
        self.Rmax_kind = []
        self.Rmin_kind = []
        self._name = "SPHERE_SAMPLING"
        self._keywords = {'Rmin': 'RMIN', 'Z_low': 'Z_LOW', 'Rmax': 'RMAX', 'X_hi': 'X_HI', 'Auto_rmax_scale': 'AUTO_RMAX_SCALE', 'X_low': 'X_LOW', 'Y_low': 'Y_LOW', 'Y_hi': 'Y_HI', 'Auto_vdw_radii_table': 'AUTO_VDW_RADII_TABLE', 'Z_hi': 'Z_HI', 'Auto_rmin_scale': 'AUTO_RMIN_SCALE'}
        self._repeated_keywords = {'Rmax_kind': 'RMAX_KIND', 'Rmin_kind': 'RMIN_KIND'}

