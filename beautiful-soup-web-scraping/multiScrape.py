
import requests;
from bs4 import BeautifulSoup;

url = 'https://scrapingclub.com/exercise/list_basic/?page=1';

website_html = requests.get(url);

#Parsing HTML doc to get a copy of HTML of the url website
soup = BeautifulSoup(website_html.text,'lxml');

#Scraping
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4');

counter = 1;

for item in items:
    itemName = item.find('h4', class_='card-title').text.strip('\n');
    itemPrice = item.find('h5').text;

    print(' %s) Item Name: %s | Item Price: %s' %(counter, itemName, itemPrice));
    counter = counter+1;


#Changing pages
pages = soup.find('url', class_='pagination');
urls = []; #List to hold the urls

links = soup.find_all('a', class_='page-link'); #All the links

for link in links:

    if(link.text.isdigit()):
        pageNum = int(link.text);
    else:
        pageNum = None;
    
    if pageNum != None:
        x = link.get('href');
        urls.append(x);

counter = 1;

#Iterating and scraping all the pages
for i in urls:
    newUrl = url + i;
    
    website = requests.get(newUrl);

    #Parsing HTML doc to get a copy of HTML of the url website
    soup = BeautifulSoup(website.text,'lxml');

    #Scraping
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4');


    for item in items:
        itemName = item.find('h4', class_='card-title').text.strip('\n');
        itemPrice = item.find('h5').text;

        print(' %s) Item Name: %s | Item Price: %s' %(counter, itemName, itemPrice));
        counter = counter+1;

