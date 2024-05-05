# org = 5
# cpy = org
# print(cpy, org)

# lst = [1, 2, 3, 4, 5]
# cplst = lst
# cplst[0] = 9
# print("Cplst:", cplst, "Lst:", lst)


# import copy
# # Shallow one level copy, then references of objects
# # Deep copy - full copy
# lst = [1, 2, 3, 4, 5]
# cplst = copy.copy(lst) # Shallow copy
# # Or
# cplst2 = lst.copy()
# # Or
# cplst3 = list(lst)
# # Or
# cplst4 = lst[:]
# cplst[0] = 9
# cplst2[0] = 19
# print("Cplst:", cplst, "Lst:", lst, "Cplst2:", cplst2)


# Deep copy (more levels deep)
import copy
mylst = [[1, 2, 3], [5, 6, 7]]
cpy = copy.deepcopy(mylst)
wrong = copy.copy(mylst) # Changes original list also
wrong[0][1] = 39
cpy[0][1] = 29
print("cpy:", cpy, "mylst:", mylst, "wrong:", wrong)


import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee 

p1 = Person('Alex', 25)
p2 = Person('Bob', 35)

company = Company(p1, p2)
# company_clone = copy.copy(company)
# company_clone.boss.age = 56

# print(company_clone.boss.age)
# print(company.boss.age)

print("***"*5)
company_clone2 = copy.deepcopy(company)
company_clone2.boss.age = 56
print(company_clone2.boss.age)
print(company.boss.age)

# Merge 2 lists, unpack
mylst = [1, 2, 3]
mylst2 = [5, 6, 7]
c = [*mylst, *mylst2]
print(c)

# Flat nested list
mylst = [[1, 2, 3], [5, 6, 7]]
result = []
for item in mylst:
    if isinstance(item, list):
        result.extend(item)
    else:
        result.append(item)
print(mylst)
print(result)
