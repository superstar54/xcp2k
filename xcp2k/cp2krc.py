#Configuration dictionary for submitting jobs
import os

# default settings
cp2krc = {
    'queue':{
          # 'account': 'psi',
          'time': '23:59:00',
          # 'nodes': '1',
          # 'ntasks-per-node': '36',
          # 'cpus-per-task': '1',
          # 'constraint': 'mc',
          # 'partition': 'normal',
          },
    'script': 'None',
      }

config_files = [os.path.join(os.environ['HOME'], '.cp2krc'),
            '.cp2krc']
for cf in config_files:
    if os.path.exists(cf):
        file = open(cf, 'r')
        cp2krc['script'] = file.read()
