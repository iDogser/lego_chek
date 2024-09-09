import requests
import re
from bs4 import BeautifulSoup

def check_item_id(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    price_block = soup.find('div', class_='c_product-top__price')
    price = price_block.text.strip() if price_block else 'Цена не найдена'

    stock_block = soup.find('div', class_='c_product-top__stock--indicator')
    if stock_block:
        stock_text = stock_block.text.strip()
        count_in_stock = int(stock_text.split()[1])
    else:
        count_in_stock = 0

    element_id_block = soup.find('li', text=lambda t: t and 'Element ID:' in t)
    if element_id_block:
        element_ids_text = element_id_block.text.split(':')[-1].strip()
        element_ids = [id.strip() for id in element_ids_text.split(',')]
    else:
        element_ids = []

    color_block = soup.find('li', text=lambda t: t and 'color:' in t)
    color = color_block.text.split(':')[-1].strip() if color_block else 'Цвет не найден'
    price = re.search(r'C\$\d+,\d+', price).group(0)
    return element_ids, price, color, count_in_stock