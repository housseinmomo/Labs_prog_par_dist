from functools import reduce
from multiprocessing import Pool, current_process, cpu_count

import numpy as np

import time

start_time = time.time()

def create_list(x):
    np.random.RandomState(100)
    arr = np.random.randint(1, 20, size=[x])
    data = arr.tolist()
    return data

def fibonacci(input):
    """Function to return the fibonacci value of the argument"""
    fiboList = []
    newValue = 0 
    for i in list:
        newValue += i
        fiboList.append(newValue)
    return fiboList

if __name__ == "__main__":
    nprocs = 2
    print("Number of cores available equals %s" % cpu_count())

    input = create_list(20)

    print("Liste aleatoire")
    print(list(input))

    #print the number of cores
    print("Number of workers equals %d" % nprocs)
   
    # create a pool of workers != number of cores 
    with Pool(processes=nprocs) as pool:
        print("test------------------")
        result = pool.map(fibonacci, list(input))
    
    total = reduce(lambda x: max(x), result)
        

    print("\n--- %s seconds ---" % (time.time() - start_time))
