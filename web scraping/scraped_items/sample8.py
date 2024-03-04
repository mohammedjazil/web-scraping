import pandas as pd 
import requests
import json
from colorama import*

with open('competitor_list.json','r') as file:
    competitor_list=json.load(file).get('competitor_list')
    
# searchterm = input("enter the item to search :")
# searchterm=searchterm.lower()

for competitor in competitor_list:
    print(Style.BRIGHT+Fore.WHITE+competitor.get('name'))
    cookie=competitor.get('cookie')
    
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie    }
        
    URL=competitor.get('cat_url')
    responses = requests.get(URL,headers=HEADERS)
    data =responses.json()
    # print(data)
    items = data.get('items')
    # for item in items:
    #     for category in item.get('categories'):
    for category in items:
            print(Style.BRIGHT+Fore.YELLOW+category.get('name'))
            print("--------------")
