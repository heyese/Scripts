
import timeit
import time
import threading
import queue
import multiprocessing as mp
# Let's experiment using threads and multi-processes ...

# Finding all the factors of a very large number
def find_num_factors(number, pause=0, num_procs=1, num_threads=1):
    """
    A convoluted function, deliberately poorly coded, which finds how many factors a given number has.
    Hopefully constructed in such a way that I can see the impact of using threads
    and multiple processes.  Intention is for multi-processes OR multi-threads, not both.

    :param number:  This is the number we are trying to find the factors of
    :param pause: after an integer is checked, sleep for this interval
    :param num_procs: uses the multiprocessing module (if > 1) to spin up given number of processes
    :param num_threads: uses the threading module (if > 1) to spin up the given number of threads
    :return:
    """
    def find_factors(number, queue, pause=0, interval=1, start=1):
        factors = 0
        for i in range(start, number, interval):
            if number % i == 0:
                factors += 1
            #  This sleep is meant to simulate possible input / output, such as reading data from a disk.
            #  The point is that inactivity causes a thread to give up the GIL, allowing another thread to do some work.
            time.sleep(pause)
        queue.put(factors)
        return factors


    # Turns out getting return values from threads isn't straight forward.
    # A queue is 'thread safe'.  In fact, multiprocessing has an implementation
    # good for both threads and processes.
    if num_procs > 1:
        q = mp.Queue()  # Special multithreaded implementation of queues.
                        # Doesn't seem to be safe with threads from threading module.
    else:
        q = queue.Queue()
    factors = 0
    # If we aren't using threads or multi processes ...
    if num_procs == 1 and num_threads == 1:
        find_factors(number, q, pause=pause)

    # Using multiple threads ...
    elif num_threads > 1:
        threads = []
        for i in range(num_threads):
            threads.append(threading.Thread(target=find_factors,
                                            args=(number, q),
                                            kwargs={'pause':pause, 'start':i + 1, 'interval':num_threads},
                                            ))
        [i.start() for i in threads]
        [i.join() for i in threads]

    elif num_threads == 1 and num_procs > 1:
        # Code something with the multiprocessing module
        # Turns out the multiprocessing module has an extremely similar api to the threading module
        procs = []
        for i in range(num_procs):
            procs.append(mp.Process(target=find_factors,
                                            args=(number, q),
                                            kwargs={'pause':pause, 'start':i + 1, 'interval':num_procs},
                                            ))
        [i.start() for i in procs]
        [i.join() for i in procs]


    else:
        print('Threads > 1 and processes > 1 at the same time is not supported')
        return

    while not q.empty():
        factors += q.get()

    return factors

#  Running this code (tick 'Run with Python Console' in Run Configurations) and then timing it for
# different values is very interesting.
#  Type in commands such as:
#  timeit.timeit('print(find_num_factors(10_000_000, pause=0.0000, num_procs=6))', number=1, globals=globals())
#  timeit.timeit('print(find_num_factors(10_000_000, pause=0.00001, num_threads=20))', number=1, globals=globals())
#  Notice that:
#      When there is no pause (so just a cpu intensive task) adding extra threads actually hinders performance,
#      due to the over head of managing the threads
#      When there is a slight pause, adding extra threads is very helpful
#      Using additional processes, up to 4, is very helpful.  The OS is able to schedule these on different cores
#      Above 4, extra processes don't help.  Because at this point they have to compete with others for a core.