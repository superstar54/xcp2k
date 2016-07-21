from xcp2k.inputsection import InputSection
from _program_banner1 import _program_banner1
from _kinetic_energy1 import _kinetic_energy1
from _derivatives1 import _derivatives1
from _neighbor_lists4 import _neighbor_lists4
from _subcell2 import _subcell2
from _ao_matrices1 import _ao_matrices1
from _mo1 import _mo1
from _mo_cubes1 import _mo_cubes1
from _stm1 import _stm1
from _wfn_mix1 import _wfn_mix1
from _gapw1 import _gapw1
from _dft_control_parameters1 import _dft_control_parameters1
from _kpoints2 import _kpoints2
from _overlap_condition1 import _overlap_condition1
from _e_density_cube1 import _e_density_cube1
from _tot_density_cube1 import _tot_density_cube1
from _v_hartree_cube1 import _v_hartree_cube1
from _external_potential_cube1 import _external_potential_cube1
from _dielectric_cube1 import _dielectric_cube1
from _dirichlet_bc_cube1 import _dirichlet_bc_cube1
from _dirichlet_cstr_charge_cube1 import _dirichlet_cstr_charge_cube1
from _v_xc_cube1 import _v_xc_cube1
from _efield_cube1 import _efield_cube1
from _elf_cube1 import _elf_cube1
from _pdos1 import _pdos1
from _moments1 import _moments1
from _mulliken1 import _mulliken1
from _lowdin1 import _lowdin1
from _hirshfeld1 import _hirshfeld1
from _xray_diffraction_spectrum1 import _xray_diffraction_spectrum1
from _electric_field_gradient1 import _electric_field_gradient1
from _basis_molopt_quantities1 import _basis_molopt_quantities1
from _hyperfine_coupling_tensor1 import _hyperfine_coupling_tensor1
from _optimize_lri_basis2 import _optimize_lri_basis2
from _plus_u1 import _plus_u1
from _sccs1 import _sccs1


class _print33(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_BANNER = _program_banner1()
        self.KINETIC_ENERGY = _kinetic_energy1()
        self.DERIVATIVES = _derivatives1()
        self.NEIGHBOR_LISTS = _neighbor_lists4()
        self.SUBCELL = _subcell2()
        self.AO_MATRICES = _ao_matrices1()
        self.MO = _mo1()
        self.MO_CUBES = _mo_cubes1()
        self.STM = _stm1()
        self.WFN_MIX = _wfn_mix1()
        self.GAPW = _gapw1()
        self.DFT_CONTROL_PARAMETERS = _dft_control_parameters1()
        self.KPOINTS = _kpoints2()
        self.OVERLAP_CONDITION = _overlap_condition1()
        self.E_DENSITY_CUBE = _e_density_cube1()
        self.TOT_DENSITY_CUBE = _tot_density_cube1()
        self.V_HARTREE_CUBE = _v_hartree_cube1()
        self.EXTERNAL_POTENTIAL_CUBE = _external_potential_cube1()
        self.DIELECTRIC_CUBE = _dielectric_cube1()
        self.DIRICHLET_BC_CUBE = _dirichlet_bc_cube1()
        self.DIRICHLET_CSTR_CHARGE_CUBE = _dirichlet_cstr_charge_cube1()
        self.V_XC_CUBE = _v_xc_cube1()
        self.EFIELD_CUBE = _efield_cube1()
        self.ELF_CUBE = _elf_cube1()
        self.PDOS = _pdos1()
        self.MOMENTS = _moments1()
        self.MULLIKEN = _mulliken1()
        self.LOWDIN = _lowdin1()
        self.HIRSHFELD = _hirshfeld1()
        self.XRAY_DIFFRACTION_SPECTRUM = _xray_diffraction_spectrum1()
        self.ELECTRIC_FIELD_GRADIENT = _electric_field_gradient1()
        self.BASIS_MOLOPT_QUANTITIES = _basis_molopt_quantities1()
        self.HYPERFINE_COUPLING_TENSOR = _hyperfine_coupling_tensor1()
        self.OPTIMIZE_LRI_BASIS = _optimize_lri_basis2()
        self.PLUS_U = _plus_u1()
        self.SCCS = _sccs1()
        self._name = "PRINT"
        self._subsections = {'DERIVATIVES': 'DERIVATIVES', 'KPOINTS': 'KPOINTS', 'AO_MATRICES': 'AO_MATRICES', 'WFN_MIX': 'WFN_MIX', 'TOT_DENSITY_CUBE': 'TOT_DENSITY_CUBE', 'OVERLAP_CONDITION': 'OVERLAP_CONDITION', 'LOWDIN': 'LOWDIN', 'DIRICHLET_BC_CUBE': 'DIRICHLET_BC_CUBE', 'XRAY_DIFFRACTION_SPECTRUM': 'XRAY_DIFFRACTION_SPECTRUM', 'EXTERNAL_POTENTIAL_CUBE': 'EXTERNAL_POTENTIAL_CUBE', 'V_XC_CUBE': 'V_XC_CUBE', 'DFT_CONTROL_PARAMETERS': 'DFT_CONTROL_PARAMETERS', 'ELECTRIC_FIELD_GRADIENT': 'ELECTRIC_FIELD_GRADIENT', 'EFIELD_CUBE': 'EFIELD_CUBE', 'V_HARTREE_CUBE': 'V_HARTREE_CUBE', 'SUBCELL': 'SUBCELL', 'DIELECTRIC_CUBE': 'DIELECTRIC_CUBE', 'STM': 'STM', 'MO_CUBES': 'MO_CUBES', 'HIRSHFELD': 'HIRSHFELD', 'DIRICHLET_CSTR_CHARGE_CUBE': 'DIRICHLET_CSTR_CHARGE_CUBE', 'GAPW': 'GAPW', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'SCCS': 'SCCS', 'MULLIKEN': 'MULLIKEN', 'HYPERFINE_COUPLING_TENSOR': 'HYPERFINE_COUPLING_TENSOR', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'MOMENTS': 'MOMENTS', 'MO': 'MO', 'OPTIMIZE_LRI_BASIS': 'OPTIMIZE_LRI_BASIS', 'PDOS': 'PDOS', 'BASIS_MOLOPT_QUANTITIES': 'BASIS_MOLOPT_QUANTITIES', 'E_DENSITY_CUBE': 'E_DENSITY_CUBE', 'ELF_CUBE': 'ELF_CUBE', 'KINETIC_ENERGY': 'KINETIC_ENERGY', 'PLUS_U': 'PLUS_U'}

