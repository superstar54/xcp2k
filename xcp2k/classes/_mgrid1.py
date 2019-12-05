from xcp2k.inputsection import InputSection
from xcp2k.classes._rs_grid2 import _rs_grid2
from xcp2k.classes._interpolator1 import _interpolator1


class _mgrid1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ngrids = None
        self.Cutoff = None
        self.Progression_factor = None
        self.Commensurate = None
        self.Realspace = None
        self.Rel_cutoff = None
        self.Multigrid_set = None
        self.Skip_load_balance_distributed = None
        self.Multigrid_cutoff = None
        self.RS_GRID_list = []
        self.INTERPOLATOR = _interpolator1()
        self._name = "MGRID"
        self._keywords = {'Ngrids': 'NGRIDS', 'Cutoff': 'CUTOFF', 'Progression_factor': 'PROGRESSION_FACTOR', 'Commensurate': 'COMMENSURATE', 'Realspace': 'REALSPACE', 'Rel_cutoff': 'REL_CUTOFF', 'Multigrid_set': 'MULTIGRID_SET', 'Skip_load_balance_distributed': 'SKIP_LOAD_BALANCE_DISTRIBUTED', 'Multigrid_cutoff': 'MULTIGRID_CUTOFF'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR'}
        self._repeated_subsections = {'RS_GRID': '_rs_grid2'}
        self._aliases = {'Relative_cutoff': 'Rel_cutoff', 'Cutoff_list': 'Multigrid_cutoff'}
        self._attributes = ['RS_GRID_list']

    def RS_GRID_add(self, section_parameters=None):
        new_section = _rs_grid2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RS_GRID_list.append(new_section)
        return new_section


    @property
    def Relative_cutoff(self):
        """
        See documentation for Rel_cutoff
        """
        return self.Rel_cutoff

    @property
    def Cutoff_list(self):
        """
        See documentation for Multigrid_cutoff
        """
        return self.Multigrid_cutoff

    @Relative_cutoff.setter
    def Relative_cutoff(self, value):
        self.Rel_cutoff = value

    @Cutoff_list.setter
    def Cutoff_list(self, value):
        self.Multigrid_cutoff = value
