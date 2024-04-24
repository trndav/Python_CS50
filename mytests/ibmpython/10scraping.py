# # Import Beautiful Soup to parse the web page content
# import requests
# from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/IBM'
# response = requests.get(url)

# # Store the HTML content in a variable
# html_content = response.text

# # Create a BeautifulSoup object to parse the HTML
# soup = BeautifulSoup(html_content, 'html.parser')
# # print(html_content[:5000])

# links = soup.find_all('a')
# for i, link in enumerate(links[:50]):
#     print(i, link.text)




import requests
import os 
from PIL import Image
from IPython.display import IFrame

# url='https://www.ibm.com/'
# r=requests.get(url)

# print(r.status_code)
# print(r.request.headers)
# print("request body:", r.request.body)
# header=r.headers
# print(r.headers)
# print("Date", header['date'])
# print("Content type:", header['Content-Type'])
# print("Content: ",r.text[0:100])

# Scrap and open image
# imgurl = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
# path = os.path.join(os.getcwd(), 'image.png')  # Saving img to comp
# r = requests.get(imgurl)
# with open(path, 'wb') as f:
#     f.write(r.content)
# Image.open(path)




# Scrap and save file
# URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
# path=os.path.join(os.getcwd(),'example1.txt')
# r = requests.get(URL)
# with open(path, 'wb') as f:
#     f.write(r.content)



# !pip install randomuser
# from randomuser import RandomUser
# import pandas as pd
# r = RandomUser()
# some_list = r.generate_users(10)
# print(some_list)
# name = r.get_full_name()
# for user in some_list:
#     print (user.get_full_name()," ",user.get_email())



# Get post
url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])


# Post request
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
print(r_post.json()['form'])


# Get randomuser API
# pip install randomuser
# from randomuser import RandomUser
# import pandas as pd
# def get_users():
#     users =[]     
#     for user in RandomUser.generate_users(10):
#         users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
#     return pd.DataFrame(users)     
# df1 = pd.DataFrame(get_users())  



# Fruityvice API
import requests
import json
import pandas as pd
data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
pd.DataFrame(results) # convert our json data into pandas data frame.
df2 = pd.json_normalize(results) # The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
print(df2)
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
print(cherry)


# Get jokes API
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results2 = json.loads(data2.text)
x = pd.DataFrame(results2)
print(x)
x.drop(columns=["id","type"],inplace=True)
print(x)

