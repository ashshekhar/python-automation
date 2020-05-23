
# Creating API requests and parsing through JSON

import requests;
import json;

# First request to API
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup';

parameters = {"upc": "0012993441012"}
response = requests.get(baseUrl, params = parameters);

print(response.url);

content = response.content; #Collected response is in JSON format, not a native data type for python
info = json.loads(content); #Converting JSON to dictionary

print(type(info));

# These are dictionary inside a dictionary
#Outermost dictionary
item = info['items'];

#The first and only dictionary inside the outermost dictionary
itemInfo = item[0];

#Pluck and print title and brand
title = itemInfo['title'];
brand = itemInfo['brand'];

print(title);
print(brand);