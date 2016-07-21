from xcp2k.inputsection import InputSection


class _job1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Directory = None
        self.Input_file_name = None
        self.Output_file_name = None
        self.Job_id = None
        self.Dependencies = None
        self._name = "JOB"
        self._keywords = {'Directory': 'DIRECTORY', 'Output_file_name': 'OUTPUT_FILE_NAME', 'Dependencies': 'DEPENDENCIES', 'Job_id': 'JOB_ID', 'Input_file_name': 'INPUT_FILE_NAME'}

