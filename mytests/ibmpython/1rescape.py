import time

for i in range(3):
    print(f"Progress: {i}/5", end='\r')
    # print(f"Progress: {i}/10")
    time.sleep(1)

print("\nTask complete!")

print(type(int(12.3)))
print(str(1+1))

x = "Fun Python"
print(x[0:5])