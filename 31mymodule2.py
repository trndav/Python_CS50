# Run like python PROGNAME ARGUMENT
import sys
from mymodule import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])