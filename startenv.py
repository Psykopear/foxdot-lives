import os
import time

from subprocess import Popen, PIPE


def is_zero_file(fpath):
    return not os.path.isfile(fpath) or os.path.getsize(fpath) == 0


if __name__ == '__main__':
    env = os.environ.copy()
    env['HOME'] = '/home/docler/.emacs-test-home'
    env['WORKON_HOME'] = '/home/docler/.virtualenvs'

    timestr = time.strftime("%Y-%m-%d")

    filename = f'/home/docler/Music/foxdot/{timestr}.py'

    init_data = '''from FoxDot import *
Clock.clear()
Scale.default=Scale.phrygian
Root.default=var(P[0], 1)
m = Master()
'''

    if is_zero_file(filename):
        with open(filename, 'w') as f:
            f.write(init_data)

    # Open emacs starting sclang right away
    os.chdir('/home/docler/Music/foxdot')
    Popen(
        ["/usr/bin/emacs", "-sclang", filename],
        stdout=PIPE,
        stdin=PIPE,
        env=env,
        bufsize=1,
        universal_newlines=True,
    )

    # with Popen(["sclang"], stdout=PIPE, stdin=PIPE, bufsize=1, universal_newlines=True) as p:
    #     for line in p.stdout:
    #         print(line, end='')
    #         if line.startswith("*** Welcome to SuperCollider 3.9.3. ***"):
    #             p.stdin.write('FoxDot.start\n')
