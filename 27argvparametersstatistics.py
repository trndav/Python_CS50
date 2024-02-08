# import statistics
# print(statistics.mean([100, 90, 80, 70]))

# Start program with python PROGNAME NAME
# import sys
# try: 
#     print("Hi! My name is", sys.argv[1])
# except IndexError:
#     print("Missing argument after name.")

# if len(sys.argv) < 2:
#     print("Not enough arguments")
# elif len(sys.argv) > 2:
#     print("Too much arguments")
# else:
#     print("Hi! My name is", sys.argv[1])

# sys.exit
# if len(sys.argv) < 2:
#     sys.exit("Not enough arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too much arguments")
# else:
#     print("Hi! My name is", sys.argv[1])
import sys
if len(sys.argv) < 2:
    sys.exit("Not enough arguments")
for arg in sys.argv[1:]:
    print(arg, end=" ")
