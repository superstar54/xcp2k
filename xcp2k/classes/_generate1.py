from xcp2k.inputsection import InputSection
from _bond2 import _bond2
from _angle1 import _angle1
from _torsion2 import _torsion2
from _improper2 import _improper2
from _isolated_atoms1 import _isolated_atoms1
from _neighbor_lists8 import _neighbor_lists8
from _print50 import _print50


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
        self.PRINT = _print50()
        self._name = "GENERATE"
        self._keywords = {'Bondlength_min': 'BONDLENGTH_MIN', 'Bondlength_max': 'BONDLENGTH_MAX', 'Bondparm': 'BONDPARM', 'Create_molecules': 'CREATE_MOLECULES', 'Bondparm_factor': 'BONDPARM_FACTOR', 'Reorder': 'REORDER'}
        self._subsections = {'PRINT': 'PRINT', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'ISOLATED_ATOMS': 'ISOLATED_ATOMS'}
        self._repeated_subsections = {'IMPROPER': '_improper2', 'TORSION': '_torsion2', 'ANGLE': '_angle1', 'BOND': '_bond2'}
        self._attributes = ['BOND_list', 'ANGLE_list', 'TORSION_list', 'IMPROPER_list']

    def IMPROPER_add(self, section_parameters=None):
        new_section = _improper2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.IMPROPER_list.append(new_section)
        return new_section

    def TORSION_add(self, section_parameters=None):
        new_section = _torsion2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.TORSION_list.append(new_section)
        return new_section

    def ANGLE_add(self, section_parameters=None):
        new_section = _angle1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.ANGLE_list.append(new_section)
        return new_section

    def BOND_add(self, section_parameters=None):
        new_section = _bond2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BOND_list.append(new_section)
        return new_section

