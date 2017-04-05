from xcp2k.inputsection import InputSection


class _powell1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Accuracy = None
        self.Step_size = None
        self.Max_fun = None
        self.Weight_pot_virtual = None
        self.Weight_pot_semicore = None
        self.Weight_pot_valence = None
        self.Weight_pot_node = None
        self.Weight_electron_configuration = None
        self.Weight_method = None
        self.Target_pot_virtual = None
        self.Target_pot_valence = None
        self.Target_pot_semicore = None
        self.Weight_psir0 = None
        self.Rcov_multiplication = None
        self._name = "POWELL"
        self._keywords = {'Rcov_multiplication': 'RCOV_MULTIPLICATION', 'Weight_pot_virtual': 'WEIGHT_POT_VIRTUAL', 'Weight_psir0': 'WEIGHT_PSIR0', 'Target_pot_valence': 'TARGET_POT_VALENCE', 'Target_pot_virtual': 'TARGET_POT_VIRTUAL', 'Max_fun': 'MAX_FUN', 'Weight_pot_valence': 'WEIGHT_POT_VALENCE', 'Weight_pot_semicore': 'WEIGHT_POT_SEMICORE', 'Step_size': 'STEP_SIZE', 'Weight_method': 'WEIGHT_METHOD', 'Target_pot_semicore': 'TARGET_POT_SEMICORE', 'Weight_electron_configuration': 'WEIGHT_ELECTRON_CONFIGURATION', 'Weight_pot_node': 'WEIGHT_POT_NODE', 'Accuracy': 'ACCURACY'}

