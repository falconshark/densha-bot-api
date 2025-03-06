import requests
from bs4 import BeautifulSoup
import string

def load_status(route_url):
    status = '通常'
    message = ''
    full_url = f'https://transit.yahoo.co.jp/{route_url}'
    route_requests = requests.get(full_url)
    route_soup = BeautifulSoup(route_requests.text, 'html.parser')
    if route_soup.find('dd',class_='trouble'):
        status = '遅延'
        message = route_soup.find('dd',class_='trouble').text
    return status, message