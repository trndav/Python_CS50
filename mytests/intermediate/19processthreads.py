# # GIL Global Interpreter Lock

# # from multiprocessing import Process 
# from threading import Thread
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         i * i 
#         time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()

# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# for p in processes:
#     p.start()

# for p in processes:
#     p.join()

# print("End main")


# GIL Global Interpreter Lock

from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i 
        time.sleep(0.1)

threads = []
num_threads = 10

for i in range(num_threads):
    p = Thread(target=square_numbers)
    threads.append(p)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End main")