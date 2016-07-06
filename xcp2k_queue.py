# -*- coding: utf-8 -*-

form xcp2k import *

  
    

def run(self):
    """Method which explicitely runs VASP."""

    # if you get here, a job is getting submitted
    script = '''
#!/bin/bash
#$ -cwd
#$ -pe openmpi 8
#$ -l s_rt=10:00:00,h_rt=10:00:30

#SGE environment
source /usr/share/Modules/init/sh
export -n -f module

#  environment modules 
#module add mpi/openmpi-1.4.3-intel-12.1
source ~/apps/cp2k-3.0/tools/toolchain/install/setup

# environment variables:
#MPIEXEC=$OPENMPI/bin/mpiexec
MPIEXEC=~/apps/cp2k-3.0/tools/toolchain/install/bin/mpiexec

export OMP_NUM_THREADS=1
export OMPI_MCA_btl='openib,sm,self'

export PYTHONPATH=~/apps/ase:$PYTHONPATH
export PATH=~/apps/ase/tools:$PATH

# The command to run with mpiexec:
#CMD=/bin/hostname
CMD=~/apps/cp2k-3.0/exe/local/cp2k_shell.psmp

ARGS=''

# The MPI command to run:
export ASE_CP2K_COMMAND="$MPIEXEC -np $NSLOTS $CMD $ARGS"


$ASE_CP2K_COMMAND

#end'''.format(**locals())

    

    cmdlist = ['qsub']
    cmdlist += ['-N', '{0}'.format(self.prefix)]
    p = Popen(cmdlist,
              stdin=PIPE, stdout=PIPE, stderr=PIPE)

    out, err = p.communicate(script)

    if out == '' or err != '':
        raise Exception('something went wrong in qsub:\n\n{0}'.format(err))

CP2K.run = run


