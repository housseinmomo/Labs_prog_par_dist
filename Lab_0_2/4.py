from __future__ import print_function

import sys


filename = sys.argv[1]

with open(filename) as f:
    for linenumber, line in enumerate(f, start=1):
        words = line.split()
        if linenumber > 5:
            break
        print("%4s: %s" % (linenumber, words[0]), end="")
