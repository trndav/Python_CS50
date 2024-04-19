# # Share data between processes
# from multiprocessing import Process, Value, Array
# import os 

# def square_numbers():
#     for i in range(1000):
#         i * i 

# if __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count() 

#     for i in range(num_processes):
#         process = Process(target=square_numbers)
#         processes.append(process)

#     for process in processes:
#         process.start()

#     for process in processes:
#         process.join()



# # Share data between processes
# # Race condition - both processes read from same add_100 number.value variable
# from multiprocessing import Process, Value, Array
# import time

# def add_100(number):
#     for i in range(100):
#         time.sleep(0.01)
#         number.value += 1

# if __name__ == "__main__":
#     shared_number = Value("i", 0) # I-integer, starting 0
#     print("Number at beginning is:", shared_number.value)

#     p1 = Process(target=add_100, args=(shared_number,))
#     p2 = Process(target=add_100, args=(shared_number,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Number at end is:", shared_number.value)



# Share data between processes
# Prevent race condition with Lock
# from multiprocessing import Process, Value, Array, Lock
# import time

# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         number.value += 1
#         lock.release()

#         # OR:        
#         # with lock:
#         #     number.value += 1

# if __name__ == "__main__":
#     lock = Lock()
#     shared_number = Value("i", 0) # I-integer, starting 0
#     # shared_array = Array('d', [0.0, 100.0, 200.0]) # 'd' - decimal
#     print("Array at beginning is:", shared_number.value)

#     p1 = Process(target=add_100, args=(shared_number, lock))
#     p2 = Process(target=add_100, args=(shared_number, lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#     print("Number at end is:", shared_number.value)




# Array
# from multiprocessing import Process, Value, Array, Lock
# import time

# def add_100(numbers, lock):
#     for i in range(10):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i] += 1
#                 print(numbers[i])

# if __name__ == "__main__":
#     lock = Lock()
#     shared_array = Array('d', [0.0, 100.0, 200.0]) # 'd' - decimal
#     print("Array at beginning is:", shared_array[:])

#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=(shared_array, lock))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("Array at end is:", shared_array[:])


# FIFO
# from multiprocessing import Process, Value, Array, Lock
# from multiprocessing import Queue
# import time

# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)

# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1*i)

# if __name__ == "__main__":
#     numbers = range(1, 6)
#     q = Queue()
#     p1 = Process(target=square, args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))
    
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     while not q.empty():
#         print(q.get())


# Multiple process that will execute process
from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()   
    # metods: map, apply, join, close
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()
    print(result)