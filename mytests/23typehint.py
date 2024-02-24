# mypy - check types

def myfunction(parameter: int) -> str: # accept int - result is str
    # print(parameter)
    return f"{parameter + 10}"

def func(param: str):
    print(param)

func(myfunction(12))

def listtype(param: list[int]): #Expecting list of integers
    return param

lst = [1,2,3,4]
print(listtype(lst))