# https://www.youtube.com/watch?v=-aKFBoZpiqA
# Python Tutorial: Context Managers - Efficiently Managing Resources

import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('temp1'):
    print(os.listdir())
with change_dir('temp2'):
    print(os.listdir())

print(os.listdir())
