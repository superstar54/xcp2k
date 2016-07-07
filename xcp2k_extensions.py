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

    if XCP2KRC['mode'] == 'run':
        # probably running at cmd line, in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode
    elif 'NHOSTS' in os.environ:
        # we are in the queue. determine if we should run serial
        # or parallel
        #NPROCS = os.environ['NSLOTS ']
        # no question. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        #parcmd = 'mpirun -np %i %s' % (NPROCS, cp2kcmd)
        exitcode = os.system(cp2kcmd)
        return exitcode
    elif 'SLURM_JOB_NODELIST' in os.environ:
        # we are in the queue. determine if we should run serial
        # or parallel
        NPROCS = int(os.environ['SLURM_NTASKS'])
        # no question. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode


    # if you get here, a job is getting submitted

    jobname = self.prefix
    #print(XCP2KRC['queue.command'])
    #print(XCP2KRC['queue.script'])

    if 'SLURM_CONF' in os.environ:
        cmdlist = ['sbatch']
        cmdlist += ['--job-name', '{0}'.format(jobname)]
    elif 'SGE_ROOT' in os.environ:
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
    
    #print(cmdlist)

    p = Popen(cmdlist,
              stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(XCP2KRC['queue.script'])

    #print(out)

    if out == '' or err != '':
        raise Exception('something went wrong in qsub:\n\n{0}'.format(err))

    import time
    #print(out)
    if 'SLURM_CONF' in os.environ:
        job_id = int(out.split()[3])
    elif 'SGE_ROOT' in os.environ:
        job_id = int(out.split()[2])
        

    delay = 1
    while True:
        if 'SLURM_CONF' in os.environ:
            output = Popen("sacct -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "COMPLETED" in output[0] and output[0].split()[15]==self.prefix:
                break
            time.sleep(delay)
        elif 'SGE_ROOT' in os.environ:
            output = Popen("qstat -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "do not exist" in output[1]:
                break
            time.sleep(delay)


CP2K.run = MethodType(run, None, CP2K)
