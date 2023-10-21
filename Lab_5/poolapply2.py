import time
from multiprocessing import Pool, current_process

start_time = time.time()

def slow_add(nsecs, x, y):
    print("Process %s going to sleep for %s second(s)" % (current_process().pid), nsecs)
    time.sleep(nsecs)
    print("Process %s waking up" % current_process().pid)
    return x + y


if __name__ == "__main__":
    print("Master process id PID %s" % current_process().pid)
    with Pool() as pool:
        # Cette fonction est utilisée pour demander à un processus spécifique dans le pool de travailleurs d'exécuter une fonction spécifiée. 
        r1 = pool.apply_async(slow_add, [5, 6, 7])
        r2 = pool.apply_async(slow_add, [3, 2, 3])
        r1.wait()
        print("Result two is %s" % r2.get())
        print("<\n--- %s secondes" % (time.time() - start_time))
    
