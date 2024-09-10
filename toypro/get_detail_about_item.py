import requests
from bs4 import BeautifulSoup
import re


import requests
from bs4 import BeautifulSoup

def get_product_block(url):
    # Запрос на страницу товара
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск блока с классом 'c_product-top'
    product_block = soup.find('div', class_='c_product-top')
    if product_block:
        category_block = product_block.find('li')
        if 'Sticker' in category_block.text:
            return product_block, True
        else:
            return product_block, False
    else:
        return None, False
    
    



def check_item_id(product_block):
    # Извлечение цены
    price_block = product_block.find('div', class_='c_product-top__price')
    price = price_block.text.strip() if price_block else 'Цена не найдена'

    # Извлечение количества на складе
    stock_block = product_block.find('div', class_='c_product-top__stock--indicator')
    if stock_block:
        stock_text = stock_block.text.strip()
        count_in_stock = int(stock_text.split()[1])
    else:
        count_in_stock = 0

    # Извлечение всех LEGO Element ID
    element_id_block = product_block.find('li', text=lambda t: t and 'Element ID:' in t)
    if element_id_block:
        element_ids_text = element_id_block.text.split(':')[-1].strip()
        element_ids = [id.strip() for id in element_ids_text.split(',')]
    else:
        element_ids = []

    # Извлечение цвета
    lego_color_block = product_block.find('li', text=lambda t: t and 'color:' in t)
    lego_color = lego_color_block.text.split(':')[-1].strip() if lego_color_block else None

    # Обычный цвет
    color_block = product_block.find('li', text=lambda t: t and 'Color:' in t)
    color = color_block.text.split(':')[-1].strip() if color_block else None

    img_element = product_block.find('img', class_='c_product-top__image')
    if img_element:
        # Извлечение значения атрибута 'src' (ссылка на изображение)
        image_url = img_element['src']
    else:
        image_url = "-"

    # Приведение цены в нужный формат
    price = re.search(r'C\$\d+,\d+', price).group(0)
    
    return element_ids, price, color, lego_color, count_in_stock, image_url
