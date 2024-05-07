with open('app.log', 'w') as f:
    f.write('Some text')

# f = open('app.log', 'w')
# try: 
#     f.write('some Text 2')
# finally:
#     f.close()

from threading import Lock 
lock = Lock()

# Not recomended - better solotuon bellow
lock.acquire()
# code
lock.release()

# Better solution
with lock:
    # code
    pass