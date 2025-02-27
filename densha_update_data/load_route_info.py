#This code is just for testing the crawler! 
#It will take very long time so don't use it.

import os
import string
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import pymysql

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

connection = pymysql.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE')
)
cursor = connection.cursor()
query = "SELECT * FROM densha_api_app_route"
cursor.execute(query)
routes = cursor.fetchall()

for route in routes:
    main_url = 'https://transit.yahoo.co.jp'
    route_url = main_url + route[3]
    route_name = route[1]
    route_requests = requests.get(route_url)
    route_soup = BeautifulSoup(route_requests.text, 'html.parser')
    if route_soup.find('dd',class_='trouble'):
        message = string.Template('${route_name}は遅延しています')
        message = message.safe_substitute({'route_name':route_name})
    else:
        message = string.Template('${route_name}は通常運転です')
        message = message.safe_substitute({'route_name':route_name})
    print(message)
    
connection.close()