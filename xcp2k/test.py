import sys
from subprocess import Popen, PIPE
import os
from os.path import join, isfile, split, islink
import numpy as np
from ase.calculators.calculator import Calculator, all_changes, Parameters
from ase.units import Rydberg
from cp2krc import *
import multiprocessing
#----------------------------------------------------------
def run(job):
    cwd = os.getcwd()
    if not os.path.exists(job):
        os.makedirs(job) 
    os.chdir(job)
    os.chdir(cwd)
#----------------------------------------------------------

n = 20
pool = multiprocessing.Pool(n)
results = []
for job in range(n):
    print('job = ', job)
    results.append(pool.apply_async(run, (str(job))))
for r in results:
    r.get()
pool.close()
pool.join()
