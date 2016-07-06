# -*- coding: utf-8 -*-

from xcp2k import *
from types import MethodType

calc = CP2K()

def run(self):
    """Monkey patch to submit job through the queue.

    If this is called, then the calculator thinks a job should be run.
    If we are in the queue, we should run it, otherwise, a job should
    be submitted.

    """

    # if we are in the queue and jasp is called or if we want to use
    # mode='run' , we should just run the job. First, we consider how.
    if 'PBS_O_WORKDIR' in os.environ or XCP2KRC['mode'] == 'run':
        log.info('In the queue. determining how to run')
        if 'PBS_NODEFILE' in os.environ:
            # we are in the queue. determine if we should run serial
            # or parallel
            NPROCS = len(open(os.environ['PBS_NODEFILE']).readlines())
            if NPROCS == 1:
                # no question. running in serial.
                cp2kcmd = XCP2KRC['cp2k.serial']
                exitcode = os.system(cp2kcmd)
                return exitcode
            else:
                # vanilla MPI run. multiprocessing does not work on more
                # than one node, and you must specify in XCP2KRC to use it
                if (XCP2KRC['queue.nodes'] > 1
                    or (XCP2KRC['queue.nodes'] == 1
                        and XCP2KRC['queue.ppn'] > 1
                        and (XCP2KRC['multiprocessing.cores_per_process']
                             == 'None'))):

                    print('MPI NPROCS = ', NPROCS)
                    cp2kcmd = XCP2KRC['cp2k.parallel']
                    parcmd = 'mpirun -np %i %s' % (NPROCS, cp2kcmd)
                    exitcode = os.system(parcmd)
                    return exitcode
                else:
                    # we need to run an MPI job on cores_per_process
                    if XCP2KRC['multiprocessing.cores_per_process'] == 1:
                        cp2kcmd = XCP2KRC['cp2k.serial']
                        exitcode = os.system(cp2kcmd)
                    elif XCP2KRC['multiprocessing.cores_per_process'] > 1:
                        NPROCS = XCP2KRC['multiprocessing.cores_per_process']

                        cp2kcmd = XCP2KRC['cp2k.parallel']
                        parcmd = 'mpirun -np %i %s' % (NPROCS, cp2kcmd)
                        exitcode = os.system(parcmd)
                        return exitcode
        else:
            # probably running at cmd line, in serial.
            cp2kcmd = XCP2KRC['cp2k.serial']
            exitcode = os.system(cp2kcmd)
            return exitcode
        # end
        # if you get here, a job is getting submitted

    jobname = self.prefix
    print(XCP2KRC['queue.command'])
    print(XCP2KRC['queue.script'])

    if 'SLURM_CONF' in os.environ:
        cmdlist = ['sbatch']
        cmdlist += ['--job-name', '{0}'.format(jobname)]
    elif 'SGE_ROOT' in os.environ:
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
    
    print(cmdlist)

    p = Popen(cmdlist,
              stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(XCP2KRC['queue.script'])

    if out == '' or err != '':
        raise Exception('something went wrong in qsub:\n\n{0}'.format(err))

    import time
    #print(out)
    job_id = int(out.split()[2])

    delay = 1
    while True:
        output = Popen("qstat -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
        if "do not exist" in output[1]:
            break
        time.sleep(delay)


CP2K.run = MethodType(run, None, CP2K)