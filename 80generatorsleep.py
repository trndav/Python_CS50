# generators - for building massive amount of data, step at time not at once

# def main():    
#     n: int = int(input("What is n? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n): # If n is to big like million, it wont even start printing
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * (i + 1))
#     return flock

# if __name__ == "__main__":
#     main()

# generators - yield - return 1 value at time
def main():    
    n: int = int(input("What is n? "))
    for s in sheep(n):
        print(s)

def sheep(n): 
    for i in range(n):
        yield "🐑" * (i + 1) # yield - return 1 value at time

if __name__ == "__main__":
    main()