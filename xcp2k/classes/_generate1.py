from xcp2k.inputsection import InputSection
from xcp2k.classes._bond2 import _bond2
from xcp2k.classes._angle1 import _angle1
from xcp2k.classes._torsion2 import _torsion2
from xcp2k.classes._improper2 import _improper2
from xcp2k.classes._isolated_atoms1 import _isolated_atoms1
from xcp2k.classes._neighbor_lists8 import _neighbor_lists8
from xcp2k.classes._print65 import _print65


class _generate1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Reorder = None
        self.Create_molecules = None
        self.Bondparm = None
        self.Bondparm_factor = None
        self.Bondlength_max = None
        self.Bondlength_min = None
        self.BOND_list = []
        self.ANGLE_list = []
        self.TORSION_list = []
        self.IMPROPER_list = []
        self.ISOLATED_ATOMS = _isolated_atoms1()
        self.NEIGHBOR_LISTS = _neighbor_lists8()
        self.PRINT = _print65()
        self._name = "GENERATE"
        self._keywords = {'Reorder': 'REORDER', 'Create_molecules': 'CREATE_MOLECULES', 'Bondparm': 'BONDPARM', 'Bondparm_factor': 'BONDPARM_FACTOR', 'Bondlength_max': 'BONDLENGTH_MAX', 'Bondlength_min': 'BONDLENGTH_MIN'}
        self._subsections = {'ISOLATED_ATOMS': 'ISOLATED_ATOMS', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'BOND': '_bond2', 'ANGLE': '_angle1', 'TORSION': '_torsion2', 'IMPROPER': '_improper2'}
        self._attributes = ['BOND_list', 'ANGLE_list', 'TORSION_list', 'IMPROPER_list']

    def BOND_add(self, section_parameters=None):
        new_section = _bond2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BOND_list.append(new_section)
        return new_section

    def ANGLE_add(self, section_parameters=None):
        new_section = _angle1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.ANGLE_list.append(new_section)
        return new_section

    def TORSION_add(self, section_parameters=None):
        new_section = _torsion2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.TORSION_list.append(new_section)
        return new_section

    def IMPROPER_add(self, section_parameters=None):
        new_section = _improper2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.IMPROPER_list.append(new_section)
        return new_section

