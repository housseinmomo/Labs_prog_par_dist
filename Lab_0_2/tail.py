from __future__ import print_function

import sys


filename = sys.argv[2]
limit = int(sys.argv[1])

with open(filename) as f:
    # on recup toutes les lignes ici
    lines = f.readlines()

    # print(lines[-1])

    print("Nombre total de lignes dans le fichier :", len(lines))
    print("-----------------------------")

    print(lines)

    linenumber = len(lines)

    for i in range(linenumber, 1):
        print("%4s: %s" % (linenumber, lines[linenumber]), end="")
        linenumber = linenumber -1

