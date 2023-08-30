from functools import reduce
from multiprocessing import Pool, cpu_count, current_process
import time

start_time = time.time()

def square(x):
    return x * x

def cube(x):
    return x * x * x

if __name__ == "__main__":
    
    r = [1, 2, 3, 4, 5]

    with Pool() as pool:
        
        result = pool.map(square, r)

        print("Square result: %s" % result)

# NB: Le problème est que le pool a été créé avant la fonction cube. Les copies travailleuses du script ont 
# donc été créées avant la définition de cube et ne contiennent donc pas une copie de cette fonction. 
# C'est l'une des raisons pour lesquelles vous devriez toujours définir vos fonctions au-dessus du bloc if 
# __name__ == "__main__". 
        
        result = pool.map(cube, r)

        print("Cube result: %s" % result)
