from xcp2k.inputsection import InputSection


class _contact1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Bandwidth = None
        self.Start = None
        self.N_atoms = None
        self.Injection_sign = None
        self.Injecting_contact = None
        self._name = "CONTACT"
        self._keywords = {'Bandwidth': 'BANDWIDTH', 'Start': 'START', 'N_atoms': 'N_ATOMS', 'Injection_sign': 'INJECTION_SIGN', 'Injecting_contact': 'INJECTING_CONTACT'}

