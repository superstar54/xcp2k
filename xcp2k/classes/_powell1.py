from xcp2k.inputsection import InputSection


class _powell1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Accuracy = None
        self.Step_size = None
        self.Max_fun = None
        self.Max_init = None
        self.Step_size_scaling = None
        self.Weight_pot_virtual = None
        self.Weight_pot_semicore = None
        self.Weight_pot_valence = None
        self.Weight_pot_node = None
        self.Weight_delta_energy = None
        self.Weight_electron_configuration = None
        self.Weight_method = None
        self.Target_pot_virtual = None
        self.Target_pot_valence = None
        self.Target_pot_semicore = None
        self.Target_delta_energy = None
        self.Target_psir0 = None
        self.Weight_psir0 = None
        self.Rcov_multiplication = None
        self.Semicore_level = None
        self._name = "POWELL"
        self._keywords = {'Rcov_multiplication': 'RCOV_MULTIPLICATION', 'Weight_pot_virtual': 'WEIGHT_POT_VIRTUAL', 'Weight_psir0': 'WEIGHT_PSIR0', 'Target_pot_valence': 'TARGET_POT_VALENCE', 'Step_size_scaling': 'STEP_SIZE_SCALING', 'Target_pot_virtual': 'TARGET_POT_VIRTUAL', 'Max_fun': 'MAX_FUN', 'Target_psir0': 'TARGET_PSIR0', 'Weight_pot_valence': 'WEIGHT_POT_VALENCE', 'Semicore_level': 'SEMICORE_LEVEL', 'Weight_pot_semicore': 'WEIGHT_POT_SEMICORE', 'Step_size': 'STEP_SIZE', 'Weight_method': 'WEIGHT_METHOD', 'Target_pot_semicore': 'TARGET_POT_SEMICORE', 'Max_init': 'MAX_INIT', 'Target_delta_energy': 'TARGET_DELTA_ENERGY', 'Weight_electron_configuration': 'WEIGHT_ELECTRON_CONFIGURATION', 'Weight_pot_node': 'WEIGHT_POT_NODE', 'Weight_delta_energy': 'WEIGHT_DELTA_ENERGY', 'Accuracy': 'ACCURACY'}

