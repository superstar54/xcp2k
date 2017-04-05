from xcp2k.inputsection import InputSection
from _acc1 import _acc1


class _dbcsr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mm_stack_size = None
        self.Mm_driver = None
        self.Avg_elements_images = None
        self.Randmat_seed = None
        self.Use_mpi_filtering = None
        self.Use_mpi_rma = None
        self.N_size_mnk_stacks = None
        self.Use_comm_thread = None
        self.Max_elements_per_block = None
        self.Comm_thread_load = None
        self.Multrec_limit = None
        self.ACC = _acc1()
        self._name = "DBCSR"
        self._keywords = {'Use_comm_thread': 'USE_COMM_THREAD', 'Multrec_limit': 'MULTREC_LIMIT', 'Mm_driver': 'MM_DRIVER', 'Comm_thread_load': 'COMM_THREAD_LOAD', 'Use_mpi_rma': 'USE_MPI_RMA', 'N_size_mnk_stacks': 'N_SIZE_MNK_STACKS', 'Randmat_seed': 'RANDMAT_SEED', 'Mm_stack_size': 'MM_STACK_SIZE', 'Use_mpi_filtering': 'USE_MPI_FILTERING', 'Max_elements_per_block': 'MAX_ELEMENTS_PER_BLOCK', 'Avg_elements_images': 'AVG_ELEMENTS_IMAGES'}
        self._subsections = {'ACC': 'ACC'}

