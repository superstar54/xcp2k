from ase.structure import molecule
from xcp2k import CP2K
from xcp2k.cp2k_example import CP2K_INPUT_OT, CP2K_INPUT_DIAG
import copy

atoms = molecule('CO')
atoms.center(vacuum=5.0)
atoms.pbc=[True, True, True]

queue = {'nodes': 1, 'ntasks-per-node': 10, 'partition': 'epyc2', 'mem-per-cpu': '5G', 'time': '23:59:00', 'config': '.cp2krc-ws-empi'}

# ===============================================================================
calc = CP2K(
    queue=queue,
    label='relax/co/co'
)
calc.CP2K_INPUT = copy.deepcopy(CP2K_INPUT_DIAG)
calc.results = {}
calc.CP2K_INPUT.GLOBAL.Run_type = "GEO_OPT"
DFT = calc.CP2K_INPUT.FORCE_EVAL_list[0].DFT
# ===============================================================================
atoms.set_calculator(calc)
e = atoms.get_potential_energy()
print('Energy: {0:1.3f}'.format(e))
