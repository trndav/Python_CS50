# Start program like python name.py -n 3

# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py [-n NUMBER]")


# argvparse  - multiple parameters, flags
# Start program like python name.py -n 3
# python .\74argvargparse.py --help
import argparse 

parser = argparse.ArgumentParser(description="Meow like a cat") # ArgumentParser() Comes with argparse
parser.add_argument("-n", default=1, help="Number of times to meow", type=int) # method in parser object
args = parser.parse_args() # 

#for _ in range(int(args.n)):
for _ in range(args.n): # if type=int is defined in add_argument
    print("meow")