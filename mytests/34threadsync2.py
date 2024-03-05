#  Threads 5. New threads cant start before old ones are released.
# Next vid https://www.youtube.com/watch?v=Kae9aV9DO7k&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=5

import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} is trying to access".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(8)
    print("{} is now released!".format(thread_number))
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)