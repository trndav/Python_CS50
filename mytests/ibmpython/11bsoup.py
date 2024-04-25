# BeautifulSoup is a Python library used for web scraping 
# from bs4 import BeautifulSoup
# import requests
# URL = "http://www.example.com"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
# print(soup)



# Scrapy is an open-source and collaborative web crawling framework
# import scrapy
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = ['http://quotes.toscrape.com/tag/humor/',]
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {'quote': quote.css('span.text::text').get()}



# Selenium is a tool used for controlling web browsers through programs and automating browser tasks.
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://www.example.com")



# Pandas
# import pandas as pd
# URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
# tables = pd.read_html(URL)
# df = tables[0]
# print(df)



# import pandas as pd
# URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
# tables = pd.read_html(URL)
# df = tables[2] # the required table will have index 2
# print(df)




# pip install html5lib
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

# html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
# <b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
# <h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
# <h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

# soup = BeautifulSoup(html, 'html5lib')
# print(soup.prettify()) # display the HTML in the nested structure

# tag_object = soup.title
# print("tag object:", tag_object)
# tag_object = soup.h3
# print(tag_object)

# tag_child = tag_object.b
# print(tag_child)
# parent_tag = tag_child.parent
# print(parent_tag)

# sibling_1 = tag_object.next_sibling
# print("Sibling", sibling_1)
# sibling_2 = sibling_1.next_sibling
# print("Sibling 2", sibling_2)

# tag_child['id']
# print(tag_child.attrs)
# print(tag_child.get('id'))

# tag_string = tag_child.string
# print(tag_string)



# #
# table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
# <td>Payload mass</td></tr><tr> <td>1</td> \
# <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
# <td>300 kg</td></tr><tr><td>2</td> \
# <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
# <td>94 kg</td></tr><tr><td>3</td> \
# <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
# <td>80 kg</td></tr></table>"

# table_bs = BeautifulSoup(table, 'html5lib')

# table_rows = table_bs.find_all('tr')
# print(table_rows)
# first_row = table_rows[0]
# print(first_row)
# print(first_row.td)

# for i, row in enumerate(table_rows):
#     print("row", i, "is", row)

# for i, row in enumerate(table_rows):
#     print("row", i)
#     cells = row.find_all('td')
#     for j, cell in enumerate(cells):
#         print('colunm', j, "cell", cell)

# list_input = table_bs.find_all(name=["td"])
# print(list_input)




# two_tables="<h3>Rocket Launch </h3> \
# <p><table class='rocket'> \
# <tr><td>Flight No</td><td>Launch site</td><td>Payload mass</td></tr> \
# <tr><td>1</td><td>Florida</td><td>300 kg</td></tr> \
# <tr><td>2</td><td>Texas</td><td>94 kg</td></tr> \
# <tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p>\
# <p><h3>Pizza Party</h3> \
# <table class='pizza'> \
# <tr><td>Pizza Place</td><td>Orders</td><td>Slices </td></tr> \
# <tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr> \
# <tr><td>Little Caesars</td><td>12</td><td >144 </td></tr> \
# <tr><td>Papa John's</td><td>15 </td><td>165</td></tr>"

# two_tables_bs = BeautifulSoup(two_tables, 'html.parser')
# print(two_tables_bs.find("table"))

# print(two_tables_bs.find("table", class_='pizza'))





# # Scrap links and images
# url = "http://www.ibm.com"
# data = requests.get(url).text
# soup = BeautifulSoup(data, "html5lib")  # create a soup object using the variable 'data'
# for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
#     print(link.get('href'))

# # Scrape all images Tags
# for link in soup.find_all('img'):  # in html image is represented by the tag <img>
#     print(link)
#     print(link.get('src'))





# Scrape data from HTML tables
# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# data = requests.get(url).text
# soup = BeautifulSoup(data, "html5lib")
# table = soup.find('table')

# for row in table.find_all('tr'):  # in html table row represented by tag <tr>
#     cols = row.find_all('td')  # in html a column is represented by tag <td>
#     color_name = cols[2].string  # store the value in column 3 as color_name
#     color_code = cols[3].text  # store the value in column 4 as color_code
#     print("{}--->{}".format(color_name, color_code))





# Scraping tables from a Web page using Pandas
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
import pandas as pd
tables = pd.read_html(url)
print(tables)



