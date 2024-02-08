# requests One of most useful package
# Make web requests like a browser
# pip install requests https://pypi.org/project/requests/

import json
import requests 
import sys 

if len(sys.argv) != 2:
    sys.exit()
    # request library converts apple JSON to Python dictionary
x = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
print(f"Requests data: {x.json()}")
print("***"*10)
print(f"JSON requests data: {json.dumps(x.json(), indent=2)}")
print("***"*10)
obj = x.json()
for result in obj["results"]: # results from apple returned data
    print(result["trackName"]) # results from trackName returned data