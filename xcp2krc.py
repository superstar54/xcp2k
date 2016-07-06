"""Configuration dictionary for submitting jobs

user.name = xingwang
user.email = xing.wang@psi.ch

mode = queue   # run|queue|None

# these are only needed if you run in a queue
queue.command = qsub
queue.options = -joe
queue.walltime = 120:00:00
queue.nodes = 1
queue.ppn = 4
queue.jobname = None

check for $HOME/.jasprc

Note that the environment variables cp2k_SERIAL and cp2k_PARALLEL can
also be used to identify the cp2k executables used by runjasp.py.

"""
import os

# default settings
XCP2KRC = {'cp2k.serial':   '$HOME/apps/cp2k-3.0/exe/local/cp2k.popt',
          'cp2k.parallel':  '$HOME/apps/cp2k-3.0/exe/local/cp2k.psmp',
          'mode': 'queue',  # other value is 'run'
          'queue.command': 'qsub',
          'queue.options': '-joe',
          'queue.walltime': '120:00:00',
          'queue.nodes': 1,
          'queue.ppn': 4,
          'queue.mem': '2GB',
          'queue.jobname': 'None',
          'queue.script': 'None',
          }


def read_configuration(fname):
    """Reads jasprc configuration from fname."""
    f = open(fname)
    for line in f:
        line = line.strip()

        if line.startswith('#'):
            pass  # comment
        elif line == '':
            pass
        else:
            if '#' in line:
                # take the part before the first #
                line = line.split('#')[0]
            key, value = line.split('=')
            XCP2KRC[key.strip()] = value.strip()
    print(XCP2KRC)

def  read_script(fname):
	file = open(fname, 'r')
	XCP2KRC['queue.script'] = file.read()


# these are the possible paths to config files, in order of increasing
# priority
config_files = [os.path.join(os.environ['HOME'], '.xcp2krc'),
                '.xcp2krc']
              
print(config_files)
for cf in config_files:
    if os.path.exists(cf):
        #read_configuration(cf)
        read_script(cf)



