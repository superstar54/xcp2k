from xcp2k.inputsection import InputSection
from _job1 import _job1
from _program_run_info45 import _program_run_info45
from _restart13 import _restart13


class _farming1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Master_slave = None
        self.Ngroups = None
        self.Group_size = None
        self.Stride = None
        self.Group_partition = None
        self.Max_jobs_per_group = None
        self.Cycle = None
        self.Wait_time = None
        self.Do_restart = None
        self.Restart_file_name = None
        self.JOB_list = []
        self.PROGRAM_RUN_INFO = _program_run_info45()
        self.RESTART = _restart13()
        self._name = "FARMING"
        self._keywords = {'Group_size': 'GROUP_SIZE', 'Restart_file_name': 'RESTART_FILE_NAME', 'Ngroups': 'NGROUPS', 'Master_slave': 'MASTER_SLAVE', 'Wait_time': 'WAIT_TIME', 'Stride': 'STRIDE', 'Group_partition': 'GROUP_PARTITION', 'Cycle': 'CYCLE', 'Do_restart': 'DO_RESTART', 'Max_jobs_per_group': 'MAX_JOBS_PER_GROUP'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'RESTART': 'RESTART'}
        self._repeated_subsections = {'JOB': '_job1'}
        self._aliases = {'Ngroup': 'Ngroups', 'Max_jobs': 'Max_jobs_per_group'}
        self._attributes = ['JOB_list']

    def JOB_add(self, section_parameters=None):
        new_section = _job1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.JOB_list.append(new_section)
        return new_section


    @property
    def Ngroup(self):
        """
        See documentation for Ngroups
        """
        return self.Ngroups

    @property
    def Max_jobs(self):
        """
        See documentation for Max_jobs_per_group
        """
        return self.Max_jobs_per_group

    @Ngroup.setter
    def Ngroup(self, value):
        self.Ngroups = value

    @Max_jobs.setter
    def Max_jobs(self, value):
        self.Max_jobs_per_group = value