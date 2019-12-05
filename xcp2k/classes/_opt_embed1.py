from xcp2k.inputsection import InputSection
from xcp2k.classes._embed_dens_diff1 import _embed_dens_diff1
from xcp2k.classes._embed_pot_cube1 import _embed_pot_cube1
from xcp2k.classes._embed_pot_vector1 import _embed_pot_vector1


class _opt_embed1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Reg_lambda = None
        self.N_iter = None
        self.Trust_rad = None
        self.Dens_conv_max = None
        self.Dens_conv_int = None
        self.Spin_dens_conv_max = None
        self.Spin_dens_conv_int = None
        self.Optimizer = None
        self.Grid_opt = None
        self.Add_const_pot = None
        self.Read_embed_pot = None
        self.Read_embed_pot_cube = None
        self.Embed_restart_file_name = None
        self.Embed_cube_file_name = None
        self.Embed_spin_cube_file_name = None
        self.EMBED_DENS_DIFF = _embed_dens_diff1()
        self.EMBED_POT_CUBE = _embed_pot_cube1()
        self.EMBED_POT_VECTOR = _embed_pot_vector1()
        self._name = "OPT_EMBED"
        self._keywords = {'Reg_lambda': 'REG_LAMBDA', 'N_iter': 'N_ITER', 'Trust_rad': 'TRUST_RAD', 'Dens_conv_max': 'DENS_CONV_MAX', 'Dens_conv_int': 'DENS_CONV_INT', 'Spin_dens_conv_max': 'SPIN_DENS_CONV_MAX', 'Spin_dens_conv_int': 'SPIN_DENS_CONV_INT', 'Optimizer': 'OPTIMIZER', 'Grid_opt': 'GRID_OPT', 'Add_const_pot': 'ADD_CONST_POT', 'Read_embed_pot': 'READ_EMBED_POT', 'Read_embed_pot_cube': 'READ_EMBED_POT_CUBE', 'Embed_restart_file_name': 'EMBED_RESTART_FILE_NAME', 'Embed_cube_file_name': 'EMBED_CUBE_FILE_NAME', 'Embed_spin_cube_file_name': 'EMBED_SPIN_CUBE_FILE_NAME'}
        self._subsections = {'EMBED_DENS_DIFF': 'EMBED_DENS_DIFF', 'EMBED_POT_CUBE': 'EMBED_POT_CUBE', 'EMBED_POT_VECTOR': 'EMBED_POT_VECTOR'}

