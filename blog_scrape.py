'''

Date - 25/02/2021
Objective- Using Beautiful soup for web scraping
Beautiful Soup Documentation -https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Example to get title link and date from a blog i.e 
"https://blog.hlab.tech/"

'''


# we import the class that we need scraping our blog

import requests
from bs4 import BeautifulSoup
from csv import writer


# we create a response variable

response = requests.get('https://blog.hlab.tech/', verify=False)

# we initialize beautiful soup and pass in our response

soup = BeautifulSoup(response.text, 'html.parser')

# we create a variable called posts and we know that our all our blog posts are in a div called blog-entry-content

posts = soup.findAll(class_='blog-entry-content')


# writing to csv file

with open('blog_scrape.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)

    # creating headers in the csv file
    headers = ['Title', 'Link', 'Date']

    # writing a row of headers in the csv
    csv_writer.writerow(headers)

    # now lets loop through our posts

    for post in posts:
        title = post.find(class_='blog-entry-title entry-title').get_text().replace('\n', '')
        link = post.find('a')['href']
        date = post.select('.blog-entry-date.clr')[0].get_text()
        csv_writer.writerow([title, link, date])