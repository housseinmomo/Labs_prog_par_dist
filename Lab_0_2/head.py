from __future__ import print_function

import sys


filename = sys.argv[2]
limit = sys.argv[1]

with open(filename) as f:
    for linenumber, line in enumerate(f, start=1):
        if linenumber > int(limit):
            break
        print("%4s: %s" % (linenumber, line), end="")
