from xcp2k.inputsection import InputSection
from _timings1 import _timings1
from _references1 import _references1
from _program_run_info1 import _program_run_info1
from _print1 import _print1
from _fm1 import _fm1
from _dbcsr1 import _dbcsr1


class _global1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Blacs_grid = None
        self.Blacs_repeatable = None
        self.Preferred_diag_library = None
        self.Elpa_kernel = None
        self.Preferred_fft_library = None
        self.Fftw_wisdom_file_name = None
        self.Fftw_plan_type = None
        self.Extended_fft_lengths = None
        self.Fft_pool_scratch_limit = None
        self.Alltoall_sgl = None
        self.Print_level = None
        self.Program_name = None
        self.Project_name = None
        self.Output_file_name = None
        self.Run_type = None
        self.Walltime = None
        self.Echo_input = None
        self.Echo_all_hosts = None
        self.Trace = None
        self.Trace_master = None
        self.Trace_max = None
        self.Trace_routines = None
        self.Flush_should_flush = None
        self.Callgraph = None
        self.Callgraph_file_name = None
        self.Seed = None
        self.Save_mem = None
        self.TIMINGS = _timings1()
        self.REFERENCES = _references1()
        self.PROGRAM_RUN_INFO = _program_run_info1()
        self.PRINT = _print1()
        self.FM = _fm1()
        self.DBCSR = _dbcsr1()
        self._name = "GLOBAL"
        self._keywords = {'Trace_routines': 'TRACE_ROUTINES', 'Save_mem': 'SAVE_MEM', 'Callgraph_file_name': 'CALLGRAPH_FILE_NAME', 'Callgraph': 'CALLGRAPH', 'Echo_all_hosts': 'ECHO_ALL_HOSTS', 'Fftw_wisdom_file_name': 'FFTW_WISDOM_FILE_NAME', 'Echo_input': 'ECHO_INPUT', 'Preferred_fft_library': 'PREFERRED_FFT_LIBRARY', 'Trace': 'TRACE', 'Alltoall_sgl': 'ALLTOALL_SGL', 'Fftw_plan_type': 'FFTW_PLAN_TYPE', 'Blacs_repeatable': 'BLACS_REPEATABLE', 'Preferred_diag_library': 'PREFERRED_DIAG_LIBRARY', 'Output_file_name': 'OUTPUT_FILE_NAME', 'Blacs_grid': 'BLACS_GRID', 'Walltime': 'WALLTIME', 'Extended_fft_lengths': 'EXTENDED_FFT_LENGTHS', 'Trace_max': 'TRACE_MAX', 'Trace_master': 'TRACE_MASTER', 'Run_type': 'RUN_TYPE', 'Project_name': 'PROJECT_NAME', 'Flush_should_flush': 'FLUSH_SHOULD_FLUSH', 'Print_level': 'PRINT_LEVEL', 'Seed': 'SEED', 'Elpa_kernel': 'ELPA_KERNEL', 'Program_name': 'PROGRAM_NAME', 'Fft_pool_scratch_limit': 'FFT_POOL_SCRATCH_LIMIT'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'TIMINGS': 'TIMINGS', 'DBCSR': 'DBCSR', 'REFERENCES': 'REFERENCES', 'PRINT': 'PRINT', 'FM': 'FM'}
        self._aliases = {'Project': 'Project_name', 'Iolevel': 'Print_level', 'Program': 'Program_name', 'Wallti': 'Walltime'}


    @property
    def Iolevel(self):
        """
        See documentation for Print_level
        """
        return self.Print_level

    @property
    def Program(self):
        """
        See documentation for Program_name
        """
        return self.Program_name

    @property
    def Project(self):
        """
        See documentation for Project_name
        """
        return self.Project_name

    @property
    def Wallti(self):
        """
        See documentation for Walltime
        """
        return self.Walltime

    @Iolevel.setter
    def Iolevel(self, value):
        self.Print_level = value

    @Program.setter
    def Program(self, value):
        self.Program_name = value

    @Project.setter
    def Project(self, value):
        self.Project_name = value

    @Wallti.setter
    def Wallti(self, value):
        self.Walltime = value
