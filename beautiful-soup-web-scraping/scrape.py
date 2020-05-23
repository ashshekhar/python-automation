
# This basically has the get function and returns a response
# containing source code from website

import requests;
from bs4 import BeautifulSoup;

#Getting HTML code
url = 'http://quotes.toscrape.com';
website_html = requests.get(url);

#Parsing HTML doc to get a copy of HTML of the url website
soup = BeautifulSoup(website_html.text,'lxml');
print(soup);

#Let's pull out quotes from this website
quotes = soup.find_all('span', class_='text');
for quote in quotes:
    print(quote.text);

#We also want authors now
authors = soup.find_all('small', class_='author');
for author in authors:
    print(author.text);

#Tags for the authors
tags = soup.find_all('div', class_='tags');
for tag in tags:
    print(tag.text);

# Formatted quotes and authors
for i in range(0,len(quotes)):
    print(quotes[i].text);
    print(authors[i].text);
    
    # This won't work as usual since it is a collection and not a single value
    quoteTags = tags[i].find_all('a',class_='tag');
    for quoteTag in quoteTags:
        print(quoteTag.text);

