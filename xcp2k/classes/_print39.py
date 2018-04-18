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
from _active_space1 import _active_space1
from _gapw1 import _gapw1
from _dft_control_parameters1 import _dft_control_parameters1
from _kpoints2 import _kpoints2
from _band_structure1 import _band_structure1
from _overlap_condition1 import _overlap_condition1
from _e_density_cube1 import _e_density_cube1
from _tot_density_cube1 import _tot_density_cube1
from _v_hartree_cube1 import _v_hartree_cube1
from _external_potential_cube1 import _external_potential_cube1
from _implicit_psolver1 import _implicit_psolver1
from _v_xc_cube1 import _v_xc_cube1
from _efield_cube1 import _efield_cube1
from _elf_cube1 import _elf_cube1
from _pdos2 import _pdos2
from _wannier901 import _wannier901
from _moments1 import _moments1
from _mulliken1 import _mulliken1
from _lowdin1 import _lowdin1
from _hirshfeld1 import _hirshfeld1
from _mao_analysis1 import _mao_analysis1
from _minbas_analysis1 import _minbas_analysis1
from _energy_windows1 import _energy_windows1
from _ks_csr_write1 import _ks_csr_write1
from _s_csr_write1 import _s_csr_write1
from _xray_diffraction_spectrum1 import _xray_diffraction_spectrum1
from _electric_field_gradient1 import _electric_field_gradient1
from _basis_molopt_quantities1 import _basis_molopt_quantities1
from _hyperfine_coupling_tensor1 import _hyperfine_coupling_tensor1
from _optimize_lri_basis2 import _optimize_lri_basis2
from _plus_u1 import _plus_u1
from _sccs1 import _sccs1


class _print39(InputSection):
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
        self.ACTIVE_SPACE = _active_space1()
        self.GAPW = _gapw1()
        self.DFT_CONTROL_PARAMETERS = _dft_control_parameters1()
        self.KPOINTS = _kpoints2()
        self.BAND_STRUCTURE = _band_structure1()
        self.OVERLAP_CONDITION = _overlap_condition1()
        self.E_DENSITY_CUBE = _e_density_cube1()
        self.TOT_DENSITY_CUBE = _tot_density_cube1()
        self.V_HARTREE_CUBE = _v_hartree_cube1()
        self.EXTERNAL_POTENTIAL_CUBE = _external_potential_cube1()
        self.IMPLICIT_PSOLVER = _implicit_psolver1()
        self.V_XC_CUBE = _v_xc_cube1()
        self.EFIELD_CUBE = _efield_cube1()
        self.ELF_CUBE = _elf_cube1()
        self.PDOS = _pdos2()
        self.WANNIER90 = _wannier901()
        self.MOMENTS = _moments1()
        self.MULLIKEN = _mulliken1()
        self.LOWDIN = _lowdin1()
        self.HIRSHFELD = _hirshfeld1()
        self.MAO_ANALYSIS = _mao_analysis1()
        self.MINBAS_ANALYSIS = _minbas_analysis1()
        self.ENERGY_WINDOWS = _energy_windows1()
        self.KS_CSR_WRITE = _ks_csr_write1()
        self.S_CSR_WRITE = _s_csr_write1()
        self.XRAY_DIFFRACTION_SPECTRUM = _xray_diffraction_spectrum1()
        self.ELECTRIC_FIELD_GRADIENT = _electric_field_gradient1()
        self.BASIS_MOLOPT_QUANTITIES = _basis_molopt_quantities1()
        self.HYPERFINE_COUPLING_TENSOR = _hyperfine_coupling_tensor1()
        self.OPTIMIZE_LRI_BASIS = _optimize_lri_basis2()
        self.PLUS_U = _plus_u1()
        self.SCCS = _sccs1()
        self._name = "PRINT"
        self._subsections = {'DERIVATIVES': 'DERIVATIVES', 'WANNIER90': 'WANNIER90', 'KPOINTS': 'KPOINTS', 'AO_MATRICES': 'AO_MATRICES', 'MAO_ANALYSIS': 'MAO_ANALYSIS', 'WFN_MIX': 'WFN_MIX', 'TOT_DENSITY_CUBE': 'TOT_DENSITY_CUBE', 'OVERLAP_CONDITION': 'OVERLAP_CONDITION', 'LOWDIN': 'LOWDIN', 'BAND_STRUCTURE': 'BAND_STRUCTURE', 'XRAY_DIFFRACTION_SPECTRUM': 'XRAY_DIFFRACTION_SPECTRUM', 'ACTIVE_SPACE': 'ACTIVE_SPACE', 'ENERGY_WINDOWS': 'ENERGY_WINDOWS', 'EXTERNAL_POTENTIAL_CUBE': 'EXTERNAL_POTENTIAL_CUBE', 'SCCS': 'SCCS', 'V_XC_CUBE': 'V_XC_CUBE', 'DFT_CONTROL_PARAMETERS': 'DFT_CONTROL_PARAMETERS', 'ELECTRIC_FIELD_GRADIENT': 'ELECTRIC_FIELD_GRADIENT', 'EFIELD_CUBE': 'EFIELD_CUBE', 'V_HARTREE_CUBE': 'V_HARTREE_CUBE', 'SUBCELL': 'SUBCELL', 'STM': 'STM', 'MO_CUBES': 'MO_CUBES', 'HIRSHFELD': 'HIRSHFELD', 'S_CSR_WRITE': 'S_CSR_WRITE', 'MINBAS_ANALYSIS': 'MINBAS_ANALYSIS', 'GAPW': 'GAPW', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'IMPLICIT_PSOLVER': 'IMPLICIT_PSOLVER', 'MULLIKEN': 'MULLIKEN', 'HYPERFINE_COUPLING_TENSOR': 'HYPERFINE_COUPLING_TENSOR', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'MOMENTS': 'MOMENTS', 'MO': 'MO', 'OPTIMIZE_LRI_BASIS': 'OPTIMIZE_LRI_BASIS', 'PDOS': 'PDOS', 'BASIS_MOLOPT_QUANTITIES': 'BASIS_MOLOPT_QUANTITIES', 'KS_CSR_WRITE': 'KS_CSR_WRITE', 'E_DENSITY_CUBE': 'E_DENSITY_CUBE', 'ELF_CUBE': 'ELF_CUBE', 'KINETIC_ENERGY': 'KINETIC_ENERGY', 'PLUS_U': 'PLUS_U'}

