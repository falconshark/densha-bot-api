from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from pathlib import Path
import os
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

main_url = 'https://transit.yahoo.co.jp/diainfo'

areas = {
    '北海道': '/area/2',
    '東北': '/area/3',
    '関東': '/area/4',
    '中部': '/area/5',
    '近畿': '/area/6',
    '中国': '/area/8',
    '四国': '/area/9',
    '九州': '/area/7',
}
        
for key, value in areas.items():
    url = main_url + value
    pageContent = ''
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        pageContent = page.content()
        browser.close()
        
    area_soup = BeautifulSoup(pageContent, 'html.parser')
    routes = area_soup.select('#mdAreaMajorLine td a')
    for route in routes:
        route_name = route.get_text()
        route_url = route['href']
        query = "INSERT INTO `densha_api_app_route` (`route_name`, `route_url`, `route_area`) VALUES (%s, %s, %s)"
        cursor.execute(query, (route_name, route_url, value))
        connection.commit()
        
connection.close()