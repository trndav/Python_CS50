
# 20argparsing.py outout.txt # optional -c -o

import sys

#def myfunction(*args, **kwargs):
#     print(args[0])
#     print(args[1])
#     print(kwargs["Key1"])
#     print(kwargs["Key2"])
# myfunction("hola", True, "something", Key1="test", Key2=5)

print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])

filename = sys.argv[1]
message = sys.argv[2]
with open(filename, "a") as f:
    f.write(message + '\n')


