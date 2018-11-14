#!/bin/bash -l
#SBATCH --account=s878
#SBATCH --job-name=xcp2k
#SBATCH --time=23:59:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=36
#SBATCH --cpus-per-task=1
#SBATCH --constraint=mc
#SBATCH --mail-user=xing.wang@psi.ch
#SBATCH --partition=normal
#========================================
# load modules and run simulation
module load daint-mc
module load cray-python
module load CP2K
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

export PYTHONPATH=~/apps/ase:$PYTHONPATH
export PYTHONPATH=~/apps/xcp2k:$PYTHONPATH

export ASE_CP2K_COMMAND="srun -n $SLURM_NTASKS --ntasks-per-node=$SLURM_NTASKS_PER_NODE -c $SLURM_CPUS_PER_TASK cp2k.psmp -i cp2k.inp -o cp2k.out"
export CP2K_DATA_DIR=/users/xingwang/apps/cp2k-4.1/data

$ASE_CP2K_COMMAND