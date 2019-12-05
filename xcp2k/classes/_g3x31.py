from xcp2k.inputsection import InputSection
from xcp2k.classes._restraint2 import _restraint2


class _g3x31(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Molecule = None
        self.Molname = None
        self.Intermolecular = None
        self.Atoms = None
        self.Distances = None
        self.Exclude_qm = None
        self.Exclude_mm = None
        self.RESTRAINT = _restraint2()
        self._name = "G3X3"
        self._keywords = {'Molecule': 'MOLECULE', 'Molname': 'MOLNAME', 'Intermolecular': 'INTERMOLECULAR', 'Atoms': 'ATOMS', 'Distances': 'DISTANCES', 'Exclude_qm': 'EXCLUDE_QM', 'Exclude_mm': 'EXCLUDE_MM'}
        self._subsections = {'RESTRAINT': 'RESTRAINT'}
        self._aliases = {'Mol': 'Molecule', 'Segname': 'Molname'}


    @property
    def Mol(self):
        """
        See documentation for Molecule
        """
        return self.Molecule

    @property
    def Segname(self):
        """
        See documentation for Molname
        """
        return self.Molname

    @Mol.setter
    def Mol(self, value):
        self.Molecule = value

    @Segname.setter
    def Segname(self, value):
        self.Molname = value
