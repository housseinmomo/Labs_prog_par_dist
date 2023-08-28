from __future__ import print_function

import sys


filename = sys.argv[1]

with open(filename) as f:
    # for line in f:
    #     print(line, end="")
    for linenumber, line in enumerate(f, start=1):
        print("%4s: %s" % (linenumber, line), end="")
