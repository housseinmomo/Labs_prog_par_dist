from functools import reduce
from multiprocessing import Pool, cpu_count, current_process
import time

start_time = time.time()

def square(x):
    print("Worker %s calculating square of %s" % (current_process().pid, x))
    return x * x

if __name__ == "__main__":

    nprocs = 2
    
    print("Number of workers  equals %s" % nprocs)

    #  Cela fournit un pool de travailleurs pouvant être utilisés pour paralléliser une opération de map. 
    # cela a créé un pool de copies travailleuses de votre script, avec autant de travailleurs que le nombre de cœurs rapporté par cpu_count()
    with Pool(processes=nprocs) as pool:
        
        r = range(1, 5001)

        # La map est répartie entre 
        # tous les travailleurs du pool. Cela signifie que si vous avez 10 travailleurs (par exemple, si vous avez 10 
        # cœurs), chaque travailleur effectuera seulement un dixième du travail

        result = pool.map(square, r)

    total = reduce(lambda x, y: x + y, result)
    
    print("The sum of square of the first 5000 integers is %s" % total) 

    print( "\n--- %s seconds ----" % (time.time() - start_time) )
