'''
Date - 25/02/2021
Objective- Using Beautiful soup for web scraping
Beautiful Soup Documentation -https://www.crummy.com/software/BeautifulSoup/bs4/doc/

'''

# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests

# ## scrap data from wikipedia

filename = "world_war_scrape.txt"
f = open(filename, 'w')
wiki=requests.get("https://en.wikipedia.org/wiki/World_War_II", verify=False)
soup=BeautifulSoup(wiki.text,'html')
print(soup.find('title'))
f.write(soup.find('title').string)


# ### find html tags with classes

ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)
    f.write(i.text)


overview=soup.find_all('table',class_='infobox vevent')
for z in overview:
    print(z.text)
    f.write(z.text)

f.close()