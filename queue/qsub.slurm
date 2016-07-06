#!/bin/bash -l
#
# CP2K on Piz Daint
#
# 256 MPI tasks, 32 nodes, 2 OpenMP threads per task, 4 Gb/task (hyperthreading)
#
# set --ntasks-per-core=1 to switch hyperthreading off and use 8 cores per node.
# Use less cores per node if you need more memory per MPI task, e.g.: 
# set --ntasks-per-node=4 for 256 tasks with 8 Gb/task on 64 nodes.
#
#SBATCH --job-name=cp2k
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#========================================
# load modules and run simulation
module load slurm
#module load cp2k
module load CP2K/3.0-CrayGNU-2016.03

export PYTHONPATH=~/apps/ase:$PYTHONPATH
export PATH=~/apps/ase/tools:$PATH

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

export ASE_CP2K_COMMAND="srun -n $SLURM_NTASKS cp2k.psmp"

# The MPI command to run: 
#MPICMD="srun -n $SLURM_NTASKS cp2k.sopt"
#echo "Command to run:"
#echo "$MPICMD"
#echo
#export ASE_CP2K_COMMAND="$MPICMD > cp2k.out"
export CP2K_DATA_DIR=/users/xingwang/apps/cp2k-3.0/data

python job.py
