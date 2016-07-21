from xcp2k.inputsection import InputSection


class _contact1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Bandwidth = None
        self.N_dof = None
        self.Start = None
        self.Injection_sign = None
        self.Injecting_contact = None
        self.N_elec = None
        self._name = "CONTACT"
        self._keywords = {'Injection_sign': 'INJECTION_SIGN', 'N_elec': 'N_ELEC', 'Start': 'START', 'Bandwidth': 'BANDWIDTH', 'N_dof': 'N_DOF', 'Injecting_contact': 'INJECTING_CONTACT'}

