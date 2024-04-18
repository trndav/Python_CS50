# Race - 2 variables run, but only 1 gets saved

# from threading import Thread
# import time
# database_value = 0
# def increase():
#     global database_value 
#     local_copy = database_value 
#     local_copy += 1
#     time.sleep(0.1)
#     database_value = local_copy

# if __name__ == "__main__":
#     print("Start value", database_value)
#     thread1 = Thread(target=increase)
#     thread2 = Thread(target=increase)

#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()

#     print("end_value", database_value)
#     print("End main")


# Locked threads
from threading import Thread, Lock
import time
database_value = 0
def increase(lock):
    global database_value 

    lock.acquire()
    local_copy = database_value 
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()

    # Same as - no need to release lock:
    # with lock:
    #     local_copy = database_value 
    #     local_copy += 1
    #     time.sleep(0.1)
    #     database_value = local_copy

if __name__ == "__main__":
    lock = Lock()
    print("Start value", database_value)
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("end_value", database_value)
    print("End main")