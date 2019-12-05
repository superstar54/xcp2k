from xcp2k.inputsection import InputSection
from xcp2k.classes._trajectory1 import _trajectory1
from xcp2k.classes._shell_trajectory1 import _shell_trajectory1
from xcp2k.classes._core_trajectory1 import _core_trajectory1
from xcp2k.classes._cell2 import _cell2
from xcp2k.classes._velocities1 import _velocities1
from xcp2k.classes._shell_velocities1 import _shell_velocities1
from xcp2k.classes._core_velocities1 import _core_velocities1
from xcp2k.classes._structure_data1 import _structure_data1
from xcp2k.classes._force_mixing_labels1 import _force_mixing_labels1
from xcp2k.classes._forces2 import _forces2
from xcp2k.classes._shell_forces1 import _shell_forces1
from xcp2k.classes._core_forces1 import _core_forces1
from xcp2k.classes._mixed_energies1 import _mixed_energies1
from xcp2k.classes._stress1 import _stress1
from xcp2k.classes._restart5 import _restart5
from xcp2k.classes._restart_history1 import _restart_history1
from xcp2k.classes._translation_vector1 import _translation_vector1


class _print16(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.TRAJECTORY = _trajectory1()
        self.SHELL_TRAJECTORY = _shell_trajectory1()
        self.CORE_TRAJECTORY = _core_trajectory1()
        self.CELL = _cell2()
        self.VELOCITIES = _velocities1()
        self.SHELL_VELOCITIES = _shell_velocities1()
        self.CORE_VELOCITIES = _core_velocities1()
        self.STRUCTURE_DATA = _structure_data1()
        self.FORCE_MIXING_LABELS = _force_mixing_labels1()
        self.FORCES = _forces2()
        self.SHELL_FORCES = _shell_forces1()
        self.CORE_FORCES = _core_forces1()
        self.MIXED_ENERGIES = _mixed_energies1()
        self.STRESS = _stress1()
        self.RESTART = _restart5()
        self.RESTART_HISTORY = _restart_history1()
        self.TRANSLATION_VECTOR = _translation_vector1()
        self._name = "PRINT"
        self._subsections = {'TRAJECTORY': 'TRAJECTORY', 'SHELL_TRAJECTORY': 'SHELL_TRAJECTORY', 'CORE_TRAJECTORY': 'CORE_TRAJECTORY', 'CELL': 'CELL', 'VELOCITIES': 'VELOCITIES', 'SHELL_VELOCITIES': 'SHELL_VELOCITIES', 'CORE_VELOCITIES': 'CORE_VELOCITIES', 'STRUCTURE_DATA': 'STRUCTURE_DATA', 'FORCE_MIXING_LABELS': 'FORCE_MIXING_LABELS', 'FORCES': 'FORCES', 'SHELL_FORCES': 'SHELL_FORCES', 'CORE_FORCES': 'CORE_FORCES', 'MIXED_ENERGIES': 'MIXED_ENERGIES', 'STRESS': 'STRESS', 'RESTART': 'RESTART', 'RESTART_HISTORY': 'RESTART_HISTORY', 'TRANSLATION_VECTOR': 'TRANSLATION_VECTOR'}

