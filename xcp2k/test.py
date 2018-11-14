# -*- coding: utf-8 -*-

from cp2k import *
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
    
    #print(os.environ)
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
        # NPROCS = int(os.environ['SLURM_NTASKS'])
        # no question. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode
    elif 'PBS_NODEFILE' in os.environ:
        # we are in the queue. determine if we should run serial
        # or parallel
        # NPROCS = int(os.environ['SLURM_NTASKS'])
        # no question明年3月, 我妈妈过来. running in serial.
        cp2kcmd = os.environ['ASE_CP2K_COMMAND']
        exitcode = os.system(cp2kcmd)
        return exitcode

    # if you get here, a job is getting submitted

    jobname = self.prefix
    #print(XCP2KRC['queue.command'])
    #print(XCP2KRC['queue.script'])

    if XCP2KRC['env'].upper() == 'SLURM':
        cmdlist = ['sbatch']
        cmdlist += ['--job-name', '{0}'.format(jobname)]
        cmdlist += ['--ntasks-per-node', '{0}'.format(self.cpu)]
    if XCP2KRC['env'].upper() == 'SGE':
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
        cmdlist += ['-pe', 'openmpi', '{0}'.format(self.cpu)]
    if XCP2KRC['env'].upper() == 'gridview':
        cmdlist = ['qsub']
        cmdlist += ['-N', '{0}'.format(jobname)]
        cmdlist += ['-l', 'nodes=1:ppn={0}'.format(self.cpu)]
        cmdlist += ['-q', 'low']
    
    #print(cmdlist)
    #print(XCP2KRC['queue.script'])

    p = Popen(cmdlist,
              stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(XCP2KRC['queue.script'])

    #print(out)
    #print(os.environ)

    if out == '' or err != '':
        raise Exception('something went wrong in qsub:\n\n{0}'.format(err))

    import time
    print(out)
    if XCP2KRC['env'].upper() == 'SLURM':
        job_id = int(out.split()[3])
    elif XCP2KRC['env'].upper() == 'SGE':
        job_id = int(out.split()[2])
    elif XCP2KRC['env'].upper() == 'gridview':
        job_id = int(out.split('.')[0]) 
    print(job_id)
        

    delay = 100 
    while True:
        if XCP2KRC['env'].upper() == 'SLURM':
            output = Popen("sacct -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "COMPLETED" in output[0] and output[0].split()[15]==self.prefix:
                break
            time.sleep(delay)
        elif XCP2KRC['env'].upper() == 'SGE':
            output = Popen("qstat -j %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "do not exist" in output[1]:
                break
            time.sleep(delay)
        elif XCP2KRC['env'].upper() == 'gridview':
            output = Popen("qstat -R %i" %(job_id), shell = True,
                   stdin = PIPE,
                   stdout = PIPE,
                   stderr = PIPE).communicate()
            if "Unknown" in output[1]:
                break
            time.sleep(delay)

