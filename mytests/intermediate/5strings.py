mystring = "Some \"string\" or 'string'"
print(mystring)

multiline = """Multi line strings
that goes in multiple lines.
Remove new line with "\\" \
character."""
print(multiline)

# Get substring, characters / slicing
string2 = "Hola there!"
char = string2[0:3]
char2 = string2[-1]
char3 = string2[::2]
char4 = string2[::-1] # Reverse
print(char, char2, char3, char4)

# Concatenate
string3 = "Hi there"
name = "Tom"
print(string3 + " " + name)

# Iterate
for i in string3:
    print(i)

if "h" in string3:
    print("yes")
else:
    print("No")

string4 = '    Hi world i!  '
print(string4.strip())
print(string4.upper().strip())
print(string4.strip().startswith("H"))
print(string4.find("i")) # Return first index
print(string4[5])
print(string4.count('i')) # Count how many times i appear

# Replace substrings
print(string4.replace('world', 'Universe'))

string5 = "How are you doing?" 
mylist = string5.split()
print(mylist)

string5 = "How,are,you,doing?" 
mylist = string5.split(",")
print(mylist)

# Join list
joined_string = ''.join(mylist)
print(joined_string) # No spaces
joined_string = ' '.join(mylist)
print(joined_string) # With spaces


list2 = ['a'] * 50000
# print(list2)

from timeit import default_timer as timer

start = timer()
# Bad code, expensive operation
mylist2 = ''
for i in list2:
    mylist2 += i
stop = timer()
print(stop-start)
# print(mylist2)

start = timer()
# Better way
mylist2 = ' '.join(list2)
stop = timer()
print(stop-start)
# print(mylist2)

# format strings
x = "Bob"
string6 = "The x is: %s" % x
print(string6)

x = 5
string6 = "The x is: %d" % x
print(string6)

x = 5.9
string6 = "The x is: %f" % x # By default, 6 digits, to specify digits use .2f
print(string6)

x = 5.9
string6 = "The x is: %.2f" % x # By default, 6 digits, to specify digits use .2f
print(string6)

x = 5.95646
string6 = "The x is: {}".format(x)
print(string6)

x = 5.95646
string6 = "The x is: {:.2f}".format(x)
print(string6)

x = 5.95646
y = 34.33
string6 = "The x is: {:.2f}, and y is: {:.2f}".format(x,y)
print(string6)

x = 5.95646
string6 = f"The x is: {x*2:.2f}"
print(string6)