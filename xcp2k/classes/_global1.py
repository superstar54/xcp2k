from xcp2k.inputsection import InputSection
from xcp2k.classes._print_elpa1 import _print_elpa1
from xcp2k.classes._timings1 import _timings1
from xcp2k.classes._references1 import _references1
from xcp2k.classes._program_run_info1 import _program_run_info1
from xcp2k.classes._print1 import _print1
from xcp2k.classes._fm1 import _fm1
from xcp2k.classes._dbcsr1 import _dbcsr1
from xcp2k.classes._fm_diag_settings1 import _fm_diag_settings1
from xcp2k.classes._grid1 import _grid1


class _global1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Blacs_grid = None
        self.Blacs_repeatable = None
        self.Preferred_diag_library = None
        self.Elpa_kernel = None
        self.Elpa_qr = None
        self.Elpa_qr_unsafe = None
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
        self.Enable_mpi_io = None
        self.Trace = None
        self.Trace_master = None
        self.Trace_max = None
        self.Trace_routines = None
        self.Flush_should_flush = None
        self.Callgraph = None
        self.Callgraph_file_name = None
        self.Seed = None
        self.Save_mem = None
        self.PRINT_ELPA = _print_elpa1()
        self.TIMINGS = _timings1()
        self.REFERENCES = _references1()
        self.PROGRAM_RUN_INFO = _program_run_info1()
        self.PRINT = _print1()
        self.FM = _fm1()
        self.DBCSR = _dbcsr1()
        self.FM_DIAG_SETTINGS = _fm_diag_settings1()
        self.GRID = _grid1()
        self._name = "GLOBAL"
        self._keywords = {'Blacs_grid': 'BLACS_GRID', 'Blacs_repeatable': 'BLACS_REPEATABLE', 'Preferred_diag_library': 'PREFERRED_DIAG_LIBRARY', 'Elpa_kernel': 'ELPA_KERNEL', 'Elpa_qr': 'ELPA_QR', 'Elpa_qr_unsafe': 'ELPA_QR_UNSAFE', 'Preferred_fft_library': 'PREFERRED_FFT_LIBRARY', 'Fftw_wisdom_file_name': 'FFTW_WISDOM_FILE_NAME', 'Fftw_plan_type': 'FFTW_PLAN_TYPE', 'Extended_fft_lengths': 'EXTENDED_FFT_LENGTHS', 'Fft_pool_scratch_limit': 'FFT_POOL_SCRATCH_LIMIT', 'Alltoall_sgl': 'ALLTOALL_SGL', 'Print_level': 'PRINT_LEVEL', 'Program_name': 'PROGRAM_NAME', 'Project_name': 'PROJECT_NAME', 'Output_file_name': 'OUTPUT_FILE_NAME', 'Run_type': 'RUN_TYPE', 'Walltime': 'WALLTIME', 'Echo_input': 'ECHO_INPUT', 'Echo_all_hosts': 'ECHO_ALL_HOSTS', 'Enable_mpi_io': 'ENABLE_MPI_IO', 'Trace': 'TRACE', 'Trace_master': 'TRACE_MASTER', 'Trace_max': 'TRACE_MAX', 'Trace_routines': 'TRACE_ROUTINES', 'Flush_should_flush': 'FLUSH_SHOULD_FLUSH', 'Callgraph': 'CALLGRAPH', 'Callgraph_file_name': 'CALLGRAPH_FILE_NAME', 'Seed': 'SEED', 'Save_mem': 'SAVE_MEM'}
        self._subsections = {'PRINT_ELPA': 'PRINT_ELPA', 'TIMINGS': 'TIMINGS', 'REFERENCES': 'REFERENCES', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'PRINT': 'PRINT', 'FM': 'FM', 'DBCSR': 'DBCSR', 'FM_DIAG_SETTINGS': 'FM_DIAG_SETTINGS', 'GRID': 'GRID'}
        self._aliases = {'Iolevel': 'Print_level', 'Program': 'Program_name', 'Project': 'Project_name', 'Wallti': 'Walltime'}


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
