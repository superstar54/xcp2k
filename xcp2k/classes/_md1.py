from xcp2k.inputsection import InputSection
from _langevin1 import _langevin1
from _msst1 import _msst1
from _barostat1 import _barostat1
from _thermostat2 import _thermostat2
from _respa1 import _respa1
from _shell1 import _shell1
from _adiabatic_dynamics1 import _adiabatic_dynamics1
from _velocity_softening1 import _velocity_softening1
from _reftraj1 import _reftraj1
from _averages1 import _averages1
from _thermal_region1 import _thermal_region1
from _print12 import _print12
from _cascade1 import _cascade1
from _initial_vibration1 import _initial_vibration1


class _md1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ensemble = None
        self.Steps = None
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
        self._keywords = {'Annealing_cell': 'ANNEALING_CELL', 'Step_start_val': 'STEP_START_VAL', 'Angvel_tol': 'ANGVEL_TOL', 'Temperature': 'TEMPERATURE', 'Angvel_zero': 'ANGVEL_ZERO', 'Econs_start_val': 'ECONS_START_VAL', 'Timestep': 'TIMESTEP', 'Initialization_method': 'INITIALIZATION_METHOD', 'Time_start_val': 'TIME_START_VAL', 'Temp_kind': 'TEMP_KIND', 'Temperature_annealing': 'TEMPERATURE_ANNEALING', 'Temp_tol': 'TEMP_TOL', 'Steps': 'STEPS', 'Displacement_tol': 'DISPLACEMENT_TOL', 'Annealing': 'ANNEALING', 'Comvel_tol': 'COMVEL_TOL', 'Scale_temp_kind': 'SCALE_TEMP_KIND', 'Ensemble': 'ENSEMBLE'}
        self._subsections = {'THERMAL_REGION': 'THERMAL_REGION', 'SHELL': 'SHELL', 'BAROSTAT': 'BAROSTAT', 'THERMOSTAT': 'THERMOSTAT', 'CASCADE': 'CASCADE', 'VELOCITY_SOFTENING': 'VELOCITY_SOFTENING', 'LANGEVIN': 'LANGEVIN', 'RESPA': 'RESPA', 'ADIABATIC_DYNAMICS': 'ADIABATIC_DYNAMICS', 'REFTRAJ': 'REFTRAJ', 'INITIAL_VIBRATION': 'INITIAL_VIBRATION', 'PRINT': 'PRINT', 'AVERAGES': 'AVERAGES', 'MSST': 'MSST'}
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
