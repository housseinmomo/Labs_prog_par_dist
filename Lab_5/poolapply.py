import time
from multiprocessing import Pool, current_process

start_time = time.time()

def slow_function(nsecs):
    print("Process %s going to sleep for %s second(s)" % (current_process().pid), nsecs)
    time.sleep(nsecs)
    print("Process %s waking up" % current_process().pid)
    return nsecs


if __name__ == "__main__":
    print("Master process id PID %s" % current_process().pid)
    with Pool() as pool:
        # Cette fonction est utilisée pour demander à un processus spécifique dans le pool de travailleurs d'exécuter une fonction spécifiée. 
        r = pool.apply(slow_function, [5])
        print("Result is %s" % r)
    print("<\n--- %s secondes" % (time.time() - start_time))
    
