'''
Date - 25/02/2021
Objective- Using Beautiful soup for web scraping
Beautiful Soup Documentation -https://www.crummy.com/software/BeautifulSoup/bs4/doc/

'''

# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url, verify=False)
htmlContent = r.content

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal
title = soup.title
# Commonly used types of objects:
# 1. Tag
print(type(title))

# 2. NavigableString
print(type(title.string))

# 3. BeautifulSoup
print(type(soup))

# 4. Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')

# Get first element in the HTML page
print(soup.find('p') ) 


# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())


# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
        linkText = link.get('href')
        all_links.add(linkText)

print(all_links)

navbarSupportedContent = soup.find(id='navbarSupportedContent')
# here 'navbarSupportedContent' replace with your id in html

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0] 
print(elem)