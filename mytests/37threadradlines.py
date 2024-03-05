
def func():
    with open("somefile.txt") as f:
        lines = f.readlines()  # Read all lines into a list
        line_index = 0
        
        while True:
            user_input = input("Enter 'y' to print the next line, or 'q' to quit: ")
            
            if user_input == 'y':
                if line_index < len(lines):
                    print(lines[line_index].strip())  # Print the next line
                    line_index += 1
                else:
                    print("End of file reached.")
                    break
func()


