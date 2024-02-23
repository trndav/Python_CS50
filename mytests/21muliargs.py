
# 20argparsing.py outout.txt # optional -c -o
# try python .\21muliargs.py -m 'Nice' -f output.txt 
# or try without arguments

import sys
import getopt # multiple args

filename = "output.txt"
message = "Awesome stuff"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

# print(opts)
# print(args)

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'a') as f:
    f.write(message + '\n')
