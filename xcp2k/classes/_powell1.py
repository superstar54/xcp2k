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
        self.Noopt_nlcc = None
        self.Preopt_nlcc = None
        self._name = "POWELL"
        self._keywords = {'Accuracy': 'ACCURACY', 'Step_size': 'STEP_SIZE', 'Max_fun': 'MAX_FUN', 'Max_init': 'MAX_INIT', 'Step_size_scaling': 'STEP_SIZE_SCALING', 'Weight_pot_virtual': 'WEIGHT_POT_VIRTUAL', 'Weight_pot_semicore': 'WEIGHT_POT_SEMICORE', 'Weight_pot_valence': 'WEIGHT_POT_VALENCE', 'Weight_pot_node': 'WEIGHT_POT_NODE', 'Weight_delta_energy': 'WEIGHT_DELTA_ENERGY', 'Weight_electron_configuration': 'WEIGHT_ELECTRON_CONFIGURATION', 'Weight_method': 'WEIGHT_METHOD', 'Target_pot_virtual': 'TARGET_POT_VIRTUAL', 'Target_pot_valence': 'TARGET_POT_VALENCE', 'Target_pot_semicore': 'TARGET_POT_SEMICORE', 'Target_delta_energy': 'TARGET_DELTA_ENERGY', 'Target_psir0': 'TARGET_PSIR0', 'Weight_psir0': 'WEIGHT_PSIR0', 'Rcov_multiplication': 'RCOV_MULTIPLICATION', 'Semicore_level': 'SEMICORE_LEVEL', 'Noopt_nlcc': 'NOOPT_NLCC', 'Preopt_nlcc': 'PREOPT_NLCC'}

