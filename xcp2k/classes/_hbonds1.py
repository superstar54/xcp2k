from xcp2k.inputsection import InputSection
from _restraint1 import _restraint1


class _hbonds1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom_type = None
        self.Molecule = None
        self.Molname = None
        self.Exclude_qm = None
        self.Exclude_mm = None
        self.Targets = None
        self.RESTRAINT = _restraint1()
        self._name = "HBONDS"
        self._keywords = {'Exclude_mm': 'EXCLUDE_MM', 'Molecule': 'MOLECULE', 'Exclude_qm': 'EXCLUDE_QM', 'Molname': 'MOLNAME', 'Targets': 'TARGETS', 'Atom_type': 'ATOM_TYPE'}
        self._subsections = {'RESTRAINT': 'RESTRAINT'}
        self._aliases = {'Segname': 'Molname'}


    @property
    def Segname(self):
        """
        See documentation for Molname
        """
        return self.Molname

    @Segname.setter
    def Segname(self, value):
        self.Molname = value
