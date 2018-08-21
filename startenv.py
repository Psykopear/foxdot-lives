import os
import time

from subprocess import Popen, PIPE


LIVE_DIR = '/home/docler/src/foxdot-lives'
INIT_DATA = '''\
FoxDot.start
from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()
'''


def is_zero_file(fpath):
    return not os.path.isfile(fpath) or os.path.getsize(fpath) == 0


if __name__ == '__main__':
    env = os.environ.copy()
    timestr = time.strftime("%Y-%m-%d")
    filename = f'{LIVE_DIR}/{timestr}.py'

    if is_zero_file(filename):
        with open(filename, 'w') as f:
            f.write(INIT_DATA)

    # Open emacs starting sclang right away
    os.chdir(LIVE_DIR)
    Popen(
        ["/usr/bin/emacs", "-sclang", filename],
        stdout=PIPE,
        stdin=PIPE,
        env=env,
        bufsize=1,
        universal_newlines=True,
    )
