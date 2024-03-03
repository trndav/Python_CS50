# https://www.youtube.com/watch?v=e05Hkz-W_aQ&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=3

import threading

def hiworld():
    for x in range(50):
        print("Hi world!")

def func2():
    for x in range(50):
        print("Two!")

t1 = threading.Thread(target=hiworld)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join() # Dont go to next statement until this code is done
print("Some weird multithreading")