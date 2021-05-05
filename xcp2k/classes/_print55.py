from xcp2k.inputsection import InputSection
from xcp2k.classes._program_banner1 import _program_banner1
from xcp2k.classes._basis_set_file1 import _basis_set_file1
from xcp2k.classes._kinetic_energy1 import _kinetic_energy1
from xcp2k.classes._derivatives1 import _derivatives1
from xcp2k.classes._neighbor_lists4 import _neighbor_lists4
from xcp2k.classes._subcell2 import _subcell2
from xcp2k.classes._ao_matrices1 import _ao_matrices1
from xcp2k.classes._mo1 import _mo1
from xcp2k.classes._mo_molden1 import _mo_molden1
from xcp2k.classes._mo_cubes1 import _mo_cubes1
from xcp2k.classes._stm1 import _stm1
from xcp2k.classes._wfn_mix1 import _wfn_mix1
from xcp2k.classes._active_space1 import _active_space1
from xcp2k.classes._gapw1 import _gapw1
from xcp2k.classes._dft_control_parameters1 import _dft_control_parameters1
from xcp2k.classes._kpoints2 import _kpoints2
from xcp2k.classes._band_structure1 import _band_structure1
from xcp2k.classes._overlap_condition1 import _overlap_condition1
from xcp2k.classes._e_density_cube1 import _e_density_cube1
from xcp2k.classes._tot_density_cube1 import _tot_density_cube1
from xcp2k.classes._v_hartree_cube1 import _v_hartree_cube1
from xcp2k.classes._external_potential_cube1 import _external_potential_cube1
from xcp2k.classes._e_density_bqb1 import _e_density_bqb1
from xcp2k.classes._voronoi1 import _voronoi1
from xcp2k.classes._implicit_psolver1 import _implicit_psolver1
from xcp2k.classes._v_xc_cube1 import _v_xc_cube1
from xcp2k.classes._efield_cube1 import _efield_cube1
from xcp2k.classes._elf_cube1 import _elf_cube1
from xcp2k.classes._local_energy_cube1 import _local_energy_cube1
from xcp2k.classes._local_stress_cube1 import _local_stress_cube1
from xcp2k.classes._dos2 import _dos2
from xcp2k.classes._pdos3 import _pdos3
from xcp2k.classes._wannier901 import _wannier901
from xcp2k.classes._moments1 import _moments1
from xcp2k.classes._mulliken1 import _mulliken1
from xcp2k.classes._lowdin1 import _lowdin1
from xcp2k.classes._hirshfeld1 import _hirshfeld1
from xcp2k.classes._mao_analysis1 import _mao_analysis1
from xcp2k.classes._minbas_analysis1 import _minbas_analysis1
from xcp2k.classes._energy_windows1 import _energy_windows1
from xcp2k.classes._ks_csr_write1 import _ks_csr_write1
from xcp2k.classes._s_csr_write1 import _s_csr_write1
from xcp2k.classes._adjmat_write1 import _adjmat_write1
from xcp2k.classes._xray_diffraction_spectrum1 import _xray_diffraction_spectrum1
from xcp2k.classes._electric_field_gradient1 import _electric_field_gradient1
from xcp2k.classes._basis_molopt_quantities1 import _basis_molopt_quantities1
from xcp2k.classes._hyperfine_coupling_tensor1 import _hyperfine_coupling_tensor1
from xcp2k.classes._optimize_lri_basis2 import _optimize_lri_basis2
from xcp2k.classes._plus_u1 import _plus_u1
from xcp2k.classes._chargemol1 import _chargemol1
from xcp2k.classes._sccs1 import _sccs1


class _print55(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_BANNER = _program_banner1()
        self.BASIS_SET_FILE = _basis_set_file1()
        self.KINETIC_ENERGY = _kinetic_energy1()
        self.DERIVATIVES = _derivatives1()
        self.NEIGHBOR_LISTS = _neighbor_lists4()
        self.SUBCELL = _subcell2()
        self.AO_MATRICES = _ao_matrices1()
        self.MO = _mo1()
        self.MO_MOLDEN = _mo_molden1()
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
        self.E_DENSITY_BQB = _e_density_bqb1()
        self.VORONOI = _voronoi1()
        self.IMPLICIT_PSOLVER = _implicit_psolver1()
        self.V_XC_CUBE = _v_xc_cube1()
        self.EFIELD_CUBE = _efield_cube1()
        self.ELF_CUBE = _elf_cube1()
        self.LOCAL_ENERGY_CUBE = _local_energy_cube1()
        self.LOCAL_STRESS_CUBE = _local_stress_cube1()
        self.DOS = _dos2()
        self.PDOS = _pdos3()
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
        self.ADJMAT_WRITE = _adjmat_write1()
        self.XRAY_DIFFRACTION_SPECTRUM = _xray_diffraction_spectrum1()
        self.ELECTRIC_FIELD_GRADIENT = _electric_field_gradient1()
        self.BASIS_MOLOPT_QUANTITIES = _basis_molopt_quantities1()
        self.HYPERFINE_COUPLING_TENSOR = _hyperfine_coupling_tensor1()
        self.OPTIMIZE_LRI_BASIS = _optimize_lri_basis2()
        self.PLUS_U = _plus_u1()
        self.CHARGEMOL = _chargemol1()
        self.SCCS = _sccs1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_BANNER': 'PROGRAM_BANNER', 'BASIS_SET_FILE': 'BASIS_SET_FILE', 'KINETIC_ENERGY': 'KINETIC_ENERGY', 'DERIVATIVES': 'DERIVATIVES', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'SUBCELL': 'SUBCELL', 'AO_MATRICES': 'AO_MATRICES', 'MO': 'MO', 'MO_MOLDEN': 'MO_MOLDEN', 'MO_CUBES': 'MO_CUBES', 'STM': 'STM', 'WFN_MIX': 'WFN_MIX', 'ACTIVE_SPACE': 'ACTIVE_SPACE', 'GAPW': 'GAPW', 'DFT_CONTROL_PARAMETERS': 'DFT_CONTROL_PARAMETERS', 'KPOINTS': 'KPOINTS', 'BAND_STRUCTURE': 'BAND_STRUCTURE', 'OVERLAP_CONDITION': 'OVERLAP_CONDITION', 'E_DENSITY_CUBE': 'E_DENSITY_CUBE', 'TOT_DENSITY_CUBE': 'TOT_DENSITY_CUBE', 'V_HARTREE_CUBE': 'V_HARTREE_CUBE', 'EXTERNAL_POTENTIAL_CUBE': 'EXTERNAL_POTENTIAL_CUBE', 'E_DENSITY_BQB': 'E_DENSITY_BQB', 'VORONOI': 'VORONOI', 'IMPLICIT_PSOLVER': 'IMPLICIT_PSOLVER', 'V_XC_CUBE': 'V_XC_CUBE', 'EFIELD_CUBE': 'EFIELD_CUBE', 'ELF_CUBE': 'ELF_CUBE', 'LOCAL_ENERGY_CUBE': 'LOCAL_ENERGY_CUBE', 'LOCAL_STRESS_CUBE': 'LOCAL_STRESS_CUBE', 'DOS': 'DOS', 'PDOS': 'PDOS', 'WANNIER90': 'WANNIER90', 'MOMENTS': 'MOMENTS', 'MULLIKEN': 'MULLIKEN', 'LOWDIN': 'LOWDIN', 'HIRSHFELD': 'HIRSHFELD', 'MAO_ANALYSIS': 'MAO_ANALYSIS', 'MINBAS_ANALYSIS': 'MINBAS_ANALYSIS', 'ENERGY_WINDOWS': 'ENERGY_WINDOWS', 'KS_CSR_WRITE': 'KS_CSR_WRITE', 'S_CSR_WRITE': 'S_CSR_WRITE', 'ADJMAT_WRITE': 'ADJMAT_WRITE', 'XRAY_DIFFRACTION_SPECTRUM': 'XRAY_DIFFRACTION_SPECTRUM', 'ELECTRIC_FIELD_GRADIENT': 'ELECTRIC_FIELD_GRADIENT', 'BASIS_MOLOPT_QUANTITIES': 'BASIS_MOLOPT_QUANTITIES', 'HYPERFINE_COUPLING_TENSOR': 'HYPERFINE_COUPLING_TENSOR', 'OPTIMIZE_LRI_BASIS': 'OPTIMIZE_LRI_BASIS', 'PLUS_U': 'PLUS_U', 'CHARGEMOL': 'CHARGEMOL', 'SCCS': 'SCCS'}

