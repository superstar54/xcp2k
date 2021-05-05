## xcp2k
CP2K Calculator for Atomic Simulation Environment (ASE).

For the introduction of ASE , please visit https://wiki.fysik.dtu.dk/ase/index.html


### Functions:
* Support all CP2K input parameters
* Automatic submit job
* Read and plot dos, pdos and layer resolved pdos
* Plot NEB

### Author
* Xing Wang  <xingwang1991@gmail.com>

### Dependencies

* ASE
* matplotlib



### Installation from source
You can get the source using git:
``` sh
git clone https://github.com/superstar54/xcp2k.git
```

Add xcp2k to your PYTHONPATH. On windows, you can edit the system environment variables.

``` sh
export PYTHONPATH="/path/to/xcp2k":$PYTHONPATH
export ASE_CP2K_COMMAND="cp2k -i cp2k.inp -o cp2k.out"
export CP2K_DATA_DIR="/path/to/data"
```


### Examples

#### CO molecule optimization
```python
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

```

#### Automatic submit job

A example of setting parameters for the queue. See example/queue.py

``` python
queue = {'nodes': 4, 
         'ntasks-per-node': 20, 
         'partition': 'all', 
         'time': '23:10:00',
         'config': 'cp2k-intel-2020b}
calc = CP2K(queue = queue)
```



#### Using default example parameters


``` python
from xcp2k.cp2k_example import CP2K_INPUT_OT, CP2K_INPUT_DIAG
calc.CP2K_INPUT = copy.deepcopy(CP2K_INPUT_DIAG)
```
