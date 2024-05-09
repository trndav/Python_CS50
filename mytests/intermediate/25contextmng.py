# with open('app.log', 'w') as f:
#     f.write('Some text')
#     print("Text successfully added")

# f = open('app.log', 'w')
# try: 
#     f.write('some Text 2')
# finally:
#     f.close()

# from threading import Lock 
# lock = Lock()

# # Not recomended - better solotuon bellow
# lock.acquire()
# # code
# lock.release()

# # Better solution
# with lock:
#     # code
#     pass

# class ManagedFile:
#     def __init__(self, filename):
#         print('init')
#         self.filename = filename

#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename, 'w')
#         return self.file 

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if self.file:
#             self.file.close()
#         if exc_type is not None:
#             print('exception has been handled')
#         print("exc:", exc_type, exc_value)
#         print('exit')
#         return True

# with ManagedFile('app.log') as file:
#     file.write('something to doo..')
#     file.doesnotexist()
#     print('printed to app.log ?? ')
# print("Continue")


from contextlib import contextmanager 
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'a')
    try: 
        yield f 
    finally:
        f.close()

with open_managed_file('app.log') as f:
    f.write('some todoo..\n')

