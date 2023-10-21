import time
from multiprocessing import Pool, cpu_count

start_time = time.time()

def slow_add(nsecs, x, y):
    print("Process %s going to sleep for %s second(s)" % (current_process().pid), nsecs)
    time.sleep(nsecs)
    return x + y

def slow_diff(nsecs, x, y):
    time.sleep(nsecs)
    return x - y

def broken_function(nsecs):
    time.sleep(nsecs)

if __name__ == "__main__":
    futures = []

    with Pool() as pool:
        futures.append(pool.apply_async(slow_add, [3, 6, 7]))
        futures.append(pool.apply_async(slow_diff, [2, 5, 2]))
        futures.append(pool.apply_async(slow_add, [1, 8, 1]))
        futures.append(pool.apply_async(broken_function, [3]))

        while True:
            all_finished = True

            print("Have the workers finished ?")

            for i, future in enumerate(futures):
                if future.ready():
                    print("Process %s has finished " % i)
                else:
                    all_finished = False
                    print("Process %s is runnign..." % i)
            
            if all_finished:
                break
            
            time.sleep()

            print("Here are the result")

            for i, future in enumerate(futures):
                if future.successful():
                    print("Process %s was successful")
                else:
                    print("Process %s failed" % i)

                    try:
                        future.get()
                    except Exception as e:
                        print("Error %s : %s" % )


if __name__ == "__main__":
    print("Master process id PID %s" % current_process().pid)
    with Pool() as pool:
        # Cette fonction est utilisée pour demander à un processus spécifique dans le pool de travailleurs d'exécuter une fonction spécifiée. 
        r1 = pool.apply_async(slow_add, [5, 6, 7])
        r2 = pool.apply_async(slow_add, [3, 2, 3])
        r1.wait()
        print("Result two is %s" % r2.get())
        print("<\n--- %s secondes" % (time.time() - start_time))
    
