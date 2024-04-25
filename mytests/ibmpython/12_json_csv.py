''' Test '''

import json
import pandas as pd
import numpy as np

df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

# add 10 to each element
df = df.transform(func = lambda x : x + 10)
print(df)
result = df.transform(func = ['sqrt'])
print(result)





# JSON file Format

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# Serializing json  
json_object = json.dumps(person, indent = 4)   
with open("sample.json", "w") as outfile: 
    outfile.write(json_object)
print(json_object)




# Read JSON from file
with open('sample.json', 'r') as openfile:   
    json_object = json.load(openfile)   
print(json_object) 
print(type(json_object))




for i in range(1,5): 
    if i!=2:
        print(i)
