from flask import Flask
import json
import requests 
from openpyxl import Workbook

app = Flask(__name__)

def item_parser(category, search_term, site):
    with open('competitors.json', 'r') as file:
        competitor = json.load(file)[site]
        
    URL = f"{competitor['store_api']}{category}/{search_term}"
    HEADERS = { 
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': competitor['cookie']
    }
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    if 'items' in data:
        items = data['items']
        for item in items:
            categories = item['categories']
            for category_dict in categories:
                if category in category_dict['name'].lower() and search_term in item['name'].lower():
                    item_found = {
                        "name": item['name'],
                        "price": item['base_price'],
                        "website": site  # Adding website name to the item_found dictionary
                    }
                    return item_found
    return None

@app.route('/api/v1/getitem/<site>/<category>/<search_term>')
def get_item(category, search_term, site):
    item = item_parser(category, search_term, site)
    if item:
        # Creating an Excel file
        wb = Workbook()
        ws = wb.active
        ws.title = "Item Data"
        ws.append(["Website", site])  
        ws.append([item["name"], item["price"]])  
        filename = f"{search_term}.xlsx"
        wb.save(filename)
        return f"Data saved to {filename}"
    else:
        return "Item not found"

if __name__ == '__main__':
    app.run(debug=True, port=5000)




#http://127.0.0.1:5000/api/v1/getitem/wegmans/apples/apple