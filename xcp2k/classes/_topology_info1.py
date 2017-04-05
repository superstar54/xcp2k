from xcp2k.inputsection import InputSection
from _each294 import _each294


class _topology_info1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Xtl_info = None
        self.Cif_info = None
        self.Pdb_info = None
        self.Xyz_info = None
        self.Psf_info = None
        self.Amber_info = None
        self.G96_info = None
        self.Crd_info = None
        self.Gtop_info = None
        self.Util_info = None
        self.Generate_info = None
        self.EACH = _each294()
        self._name = "TOPOLOGY_INFO"
        self._keywords = {'Gtop_info': 'GTOP_INFO', 'Log_print_key': 'LOG_PRINT_KEY', 'Xyz_info': 'XYZ_INFO', 'Crd_info': 'CRD_INFO', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'G96_info': 'G96_INFO', 'Xtl_info': 'XTL_INFO', 'Pdb_info': 'PDB_INFO', 'Add_last': 'ADD_LAST', 'Util_info': 'UTIL_INFO', 'Generate_info': 'GENERATE_INFO', 'Cif_info': 'CIF_INFO', 'Psf_info': 'PSF_INFO', 'Filename': 'FILENAME', 'Amber_info': 'AMBER_INFO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

