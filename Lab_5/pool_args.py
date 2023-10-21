from functools import reduce
from multiprocessing import Pool, cpu_count
import time 

# On lance le compteur 
start_time = time.time()

def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

if __name__ == "__main__":
    # Nombre de coeurs disponible 
    print("Number of core available equals %s" % cpu_count())

    # Creation d'un pool de travailleur 
    with Pool() as pool:
        # tableau de somme des deux autres tableau 
        result = pool.starmap(add, zip(a, b))
    
    # on fait la somme total 
    total = reduce(lambda x, y: x + y, result)

    print("The sum of a and b is %s" % total)
    
    print("<\n--- %s secondes" % (time.time() - start_time))