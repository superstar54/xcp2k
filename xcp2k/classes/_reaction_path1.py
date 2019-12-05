from xcp2k.inputsection import InputSection
from xcp2k.classes._colvar2 import _colvar2
from xcp2k.classes._frame3 import _frame3
from xcp2k.classes._map1 import _map1


class _reaction_path1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Distances_rmsd = None
        self.Rmsd = None
        self.Subset_type = None
        self.Align_frames = None
        self.Atoms = []
        self.Function = []
        self.Variable = None
        self.Lambda = None
        self.Step_size = None
        self.Range = None
        self.COLVAR_list = []
        self.FRAME_list = []
        self.MAP = _map1()
        self._name = "REACTION_PATH"
        self._keywords = {'Distances_rmsd': 'DISTANCES_RMSD', 'Rmsd': 'RMSD', 'Subset_type': 'SUBSET_TYPE', 'Align_frames': 'ALIGN_FRAMES', 'Variable': 'VARIABLE', 'Lambda': 'LAMBDA', 'Step_size': 'STEP_SIZE', 'Range': 'RANGE'}
        self._repeated_keywords = {'Atoms': 'ATOMS', 'Function': 'FUNCTION'}
        self._subsections = {'MAP': 'MAP'}
        self._repeated_subsections = {'COLVAR': '_colvar2', 'FRAME': '_frame3'}
        self._attributes = ['COLVAR_list', 'FRAME_list']

    def COLVAR_add(self, section_parameters=None):
        new_section = _colvar2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.COLVAR_list.append(new_section)
        return new_section

    def FRAME_add(self, section_parameters=None):
        new_section = _frame3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAME_list.append(new_section)
        return new_section

