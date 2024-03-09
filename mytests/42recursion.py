# https://www.youtube.com/watch?v=OYnf6mr7uow&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=9
# 9! - factorial of 9 = 9*8*7*6*5*4*3*2*1
# 9! = 9 * 8!

n = 7
fact = 1
while n > 0:
    fact = fact * n
    n-= 1
print(fact)

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
    return number 
print(factorial(7))

print("*******"*5)

# Fibonacci 0, 1, 1, 2, 3, 5, 8 last+current
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
        print(a)
    return f"Fibonnacci of {n} is {a}."

print(fibonacci(50))

print("*******"*5)

# Recursive

def fibonacci2(n):
    if n <= 1:
        return n
    else: 
        return (fibonacci2(n-1) + fibonacci2(n-2))
    
print(fibonacci2(50))
