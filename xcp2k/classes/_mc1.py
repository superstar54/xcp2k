from xcp2k.inputsection import InputSection
from xcp2k.classes._avbmc1 import _avbmc1
from xcp2k.classes._move_probabilities1 import _move_probabilities1
from xcp2k.classes._move_updates1 import _move_updates1
from xcp2k.classes._max_displacements1 import _max_displacements1


class _mc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nstep = None
        self.Iprint = None
        self.Nmoves = None
        self.Nswapmoves = None
        self.Lbias = None
        self.Lstop = None
        self.Ldiscrete = None
        self.Rclus = None
        self.Restart = None
        self.Nvirial = None
        self.Ensemble = None
        self.Restart_file_name = None
        self.Moves_file_name = None
        self.Molecules_file_name = None
        self.Coordinate_file_name = None
        self.Energy_file_name = None
        self.Data_file_name = None
        self.Cell_file_name = None
        self.Max_disp_file_name = None
        self.Box2_file_name = None
        self.Pressure = None
        self.Temperature = None
        self.Virial_temps = None
        self.Discrete_step = None
        self.Eta = None
        self.Randomtoskip = None
        self.AVBMC = _avbmc1()
        self.MOVE_PROBABILITIES = _move_probabilities1()
        self.MOVE_UPDATES = _move_updates1()
        self.MAX_DISPLACEMENTS = _max_displacements1()
        self._name = "MC"
        self._keywords = {'Nstep': 'NSTEP', 'Iprint': 'IPRINT', 'Nmoves': 'NMOVES', 'Nswapmoves': 'NSWAPMOVES', 'Lbias': 'LBIAS', 'Lstop': 'LSTOP', 'Ldiscrete': 'LDISCRETE', 'Rclus': 'RCLUS', 'Restart': 'RESTART', 'Nvirial': 'NVIRIAL', 'Ensemble': 'ENSEMBLE', 'Restart_file_name': 'RESTART_FILE_NAME', 'Moves_file_name': 'MOVES_FILE_NAME', 'Molecules_file_name': 'MOLECULES_FILE_NAME', 'Coordinate_file_name': 'COORDINATE_FILE_NAME', 'Energy_file_name': 'ENERGY_FILE_NAME', 'Data_file_name': 'DATA_FILE_NAME', 'Cell_file_name': 'CELL_FILE_NAME', 'Max_disp_file_name': 'MAX_DISP_FILE_NAME', 'Box2_file_name': 'BOX2_FILE_NAME', 'Pressure': 'PRESSURE', 'Temperature': 'TEMPERATURE', 'Virial_temps': 'VIRIAL_TEMPS', 'Discrete_step': 'DISCRETE_STEP', 'Eta': 'ETA', 'Randomtoskip': 'RANDOMTOSKIP'}
        self._subsections = {'AVBMC': 'AVBMC', 'MOVE_PROBABILITIES': 'MOVE_PROBABILITIES', 'MOVE_UPDATES': 'MOVE_UPDATES', 'MAX_DISPLACEMENTS': 'MAX_DISPLACEMENTS'}

