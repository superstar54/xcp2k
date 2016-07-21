from xcp2k.inputsection import InputSection


class _periodic_efield1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Intensity = None
        self.Polarisation = None
        self.Displacement_field = None
        self._name = "PERIODIC_EFIELD"
        self._keywords = {'Intensity': 'INTENSITY', 'Displacement_field': 'DISPLACEMENT_FIELD', 'Polarisation': 'POLARISATION'}

