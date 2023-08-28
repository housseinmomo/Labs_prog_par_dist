from __future__ import print_function

import sys


filename = sys.argv[1]

with open(filename) as f:
    for linenumber, line in enumerate(f, start=1):
        if linenumber == 1: 
            continue
        words = line.split()
        print("%4s: %s" % (linenumber, words), end="")
