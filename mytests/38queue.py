import queue

mylist = [10, 20, 30, 40, 50, 60, 70]

# q = queue.Queue() # FIFO
# q = queue.LifoQueue() # LIFO
q = queue.PriorityQueue() # Add priorities in tuple

q.put((3, "Third"))
q.put((1, "Hola! First queue!"))
q.put((4, "Forth queue"))
q.put((2, 2))

while not q.empty():
    print(q.get()[1]) # print second element of PriorityQueue

# print(q.get())
# print(q.get())
# print(q.get())