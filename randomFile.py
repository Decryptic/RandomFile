#!/usr/bin/env python3

from os      import getcwd, listdir
from os.path import isfile, join, basename
from random  import randrange

def main():
    cwd = getcwd()
    base = basename(__file__)
    files = [ f for f in listdir(cwd) if isfile(join(cwd, f)) and f != base ]
    n = len(files)
    if n > 0:
        print(files[randrange(n)])

main()
