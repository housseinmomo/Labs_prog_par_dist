from functools import reduce
import time

start_time = time.time()

print(__name__)

# vous devez vous assurer que seule la copie maîtresse du script exécute le code
if __name__ == "__main__":
    
    r = range(1, 5001)

    result = map(lambda x: x * x, r)

    total = reduce(lambda x, y: x + y, result)

    print("The sum of square of the first 5000 integers is %s" % total) 

    print( "\n--- %s seconds ----" % (time.time() - start_time) )