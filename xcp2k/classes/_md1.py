from xcp2k.inputsection import InputSection
from xcp2k.classes._langevin1 import _langevin1
from xcp2k.classes._msst1 import _msst1
from xcp2k.classes._barostat1 import _barostat1
from xcp2k.classes._thermostat2 import _thermostat2
from xcp2k.classes._respa1 import _respa1
from xcp2k.classes._shell1 import _shell1
from xcp2k.classes._adiabatic_dynamics1 import _adiabatic_dynamics1
from xcp2k.classes._velocity_softening1 import _velocity_softening1
from xcp2k.classes._reftraj1 import _reftraj1
from xcp2k.classes._averages1 import _averages1
from xcp2k.classes._thermal_region1 import _thermal_region1
from xcp2k.classes._print12 import _print12
from xcp2k.classes._cascade1 import _cascade1
from xcp2k.classes._initial_vibration1 import _initial_vibration1


class _md1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ensemble = None
        self.Steps = None
        self.Max_steps = None
        self.Timestep = None
        self.Step_start_val = None
        self.Time_start_val = None
        self.Econs_start_val = None
        self.Temperature = None
        self.Temp_tol = None
        self.Temp_kind = None
        self.Scale_temp_kind = None
        self.Comvel_tol = None
        self.Angvel_tol = None
        self.Angvel_zero = None
        self.Annealing = None
        self.Annealing_cell = None
        self.Temperature_annealing = None
        self.Displacement_tol = None
        self.Initialization_method = None
        self.LANGEVIN = _langevin1()
        self.MSST = _msst1()
        self.BAROSTAT = _barostat1()
        self.THERMOSTAT = _thermostat2()
        self.RESPA = _respa1()
        self.SHELL = _shell1()
        self.ADIABATIC_DYNAMICS = _adiabatic_dynamics1()
        self.VELOCITY_SOFTENING = _velocity_softening1()
        self.REFTRAJ = _reftraj1()
        self.AVERAGES = _averages1()
        self.THERMAL_REGION = _thermal_region1()
        self.PRINT = _print12()
        self.CASCADE = _cascade1()
        self.INITIAL_VIBRATION = _initial_vibration1()
        self._name = "MD"
        self._keywords = {'Ensemble': 'ENSEMBLE', 'Steps': 'STEPS', 'Max_steps': 'MAX_STEPS', 'Timestep': 'TIMESTEP', 'Step_start_val': 'STEP_START_VAL', 'Time_start_val': 'TIME_START_VAL', 'Econs_start_val': 'ECONS_START_VAL', 'Temperature': 'TEMPERATURE', 'Temp_tol': 'TEMP_TOL', 'Temp_kind': 'TEMP_KIND', 'Scale_temp_kind': 'SCALE_TEMP_KIND', 'Comvel_tol': 'COMVEL_TOL', 'Angvel_tol': 'ANGVEL_TOL', 'Angvel_zero': 'ANGVEL_ZERO', 'Annealing': 'ANNEALING', 'Annealing_cell': 'ANNEALING_CELL', 'Temperature_annealing': 'TEMPERATURE_ANNEALING', 'Displacement_tol': 'DISPLACEMENT_TOL', 'Initialization_method': 'INITIALIZATION_METHOD'}
        self._subsections = {'LANGEVIN': 'LANGEVIN', 'MSST': 'MSST', 'BAROSTAT': 'BAROSTAT', 'THERMOSTAT': 'THERMOSTAT', 'RESPA': 'RESPA', 'SHELL': 'SHELL', 'ADIABATIC_DYNAMICS': 'ADIABATIC_DYNAMICS', 'VELOCITY_SOFTENING': 'VELOCITY_SOFTENING', 'REFTRAJ': 'REFTRAJ', 'AVERAGES': 'AVERAGES', 'THERMAL_REGION': 'THERMAL_REGION', 'PRINT': 'PRINT', 'CASCADE': 'CASCADE', 'INITIAL_VIBRATION': 'INITIAL_VIBRATION'}
        self._aliases = {'Temp_to': 'Temp_tol', 'Temperature_tolerance': 'Temp_tol'}


    @property
    def Temp_to(self):
        """
        See documentation for Temp_tol
        """
        return self.Temp_tol

    @property
    def Temperature_tolerance(self):
        """
        See documentation for Temp_tol
        """
        return self.Temp_tol

    @Temp_to.setter
    def Temp_to(self, value):
        self.Temp_tol = value

    @Temperature_tolerance.setter
    def Temperature_tolerance(self, value):
        self.Temp_tol = value
