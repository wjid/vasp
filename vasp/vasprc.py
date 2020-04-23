"""Configuration dictionary for submitting jobs
mode = queue   # this defines whether jobs are immediately run or queued
user.name = jkitchin
user.email = jkitchin@andrew.cmu.edu
queue.command = qsub
queue.options = -joe
queue.walltime = 168:00:00
queue.nodes = 1
queue.ppn = 1
queue.mem = 2GB
queue.jobname = None
check for $HOME/.vasprc
then check for ./.vasprc
Note that the environment variables VASP_SERIAL and VASP_PARALLEL can
also be used to identify the vasp executables used by runvasp.py.
"""
import os

vs = '/Users/wjid/VASP/src/vaspSol.5.4.1/bin/vasp_std'
vp = '/Users/wjid/VASP/src/vaspSol.5.4.1/bin/vasp_std

# default settings
VASPRC = {'vasp.executable.serial': vs,
          'vasp.executable.parallel': vp,
          'mode': 'run',  # other value is 'queue'
          'queue.command': 'qsub',
          'queue.options': '-joe',
          'queue.walltime': '168:00:00',
          'queue.nodes': 1,
          'queue.ppn': 1,
          'queue.mem': '2GB',
          'queue.jobname': 'None',
          'multiprocessing.cores_per_process': 'None',
          'vdw_kernel.bindat':
          '/Users/wjid/VASP/vdw_kernel.bindat',
          'restart_unconverged': True,
          'validate': False,
          'handle_exceptions': True
          }


def read_configuration(fname='.vasprc'):
    """Reads vasprc configuration from fname."""
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
            VASPRC[key.strip()] = value.strip()

# these are the possible paths to config files, in order of increasing
# priority
config_files = [os.path.join(os.environ['HOME'], '.vasprc'),
                '.vasprc']

for cf in config_files:
    if os.path.exists(cf):
        read_configuration(cf)
