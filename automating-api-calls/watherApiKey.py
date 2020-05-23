
# Implementing APIs which use unique keys
import requests;

baseUrl = 'https://api.openweathermap.org/data/2.5/forecast';


#Based on the API Call instructions on the website, we define the following
#APPID is a unique key generating on creating account on the baseUrl
parameters = {'APPID': '87470be0d3f12b03e09381b6fa2f9dd9','q':'Seattle,US'}; 

response = requests.get(baseUrl,params=parameters);

# Printing the JSON Content
print(response.content);
