from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import json
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

routes_info = []
        
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
        route_info = {
            'route_name': route_name,
            'route_area_name': key,
            'route_area_url': value,
            'route_url': route_url,
        }
        routes_info.append(route_info)
        
with open('../route_data.json', 'w') as f:
    json.dump(routes_info, f)
        