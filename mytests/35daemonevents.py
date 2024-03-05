# https://www.youtube.com/watch?v=Kae9aV9DO7k&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=5

import threading

event = threading.Event()

def func():
    print("Waiting for event to trigger..\n")
    event.wait()
    print("Performing action XYZ...\n")

t1 = threading.Thread(target=func)
t1.start()

x = input("Do you want to trigger event? (y/n)")
if x == "y":
    event.set()