import requests
import re
from bs4 import BeautifulSoup

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
    area_requests = requests.get(url)
    area_soup = BeautifulSoup(area_requests.text, 'html.parser')
    routes = area_soup.select('dd a')
    for route in routes:
        route_url = route.attrs['href']
        route_name = route.get_text()
        if len(re.findall('.+列車遅延|.+運転再開|.+平常運転|.+運転情報|.+見合わせ|.+運転状況|.+その他', route_name)) == 0:
            route = {
                'name': route_name,
                'url': route_url,
                'type': 
            }