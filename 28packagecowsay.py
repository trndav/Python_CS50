import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hi, " + sys.argv[1])
    cowsay.trex("Hi, " + sys.argv[1])