# https://www.youtube.com/watch?v=F3-bJlYWeJc&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=4
# Locking . only 1 thread at the time can use resource

import threading
import time

x = 512
lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    while x < 1024:
        x *= 2
        time.sleep(1)
        print(x)    
    print("Reached the maximum")
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)    
        time.sleep(1)
    print("Reached the minimum")
    lock.release()

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()