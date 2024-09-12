import requests
from bs4 import BeautifulSoup

def search_and_extract_product_info(item_id):
    # URL для поиска по ID
    search_url = f"https://www.lego.com/en-us/pick-and-build/pick-a-brick?includeOutOfStock=true&query={item_id}&perPage=400"
    
    # Выполняем запрос на страницу
    response = requests.get(search_url)
    if response.status_code != 200:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        return None, None, None, None
    
    # Парсим HTML-ответ
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все блоки с товарами
    product_blocks = soup.find_all('li', class_='ElementsList_leaf__3tVNf ElementsList_row-count-4__HKOE5')
    
    if not product_blocks:
        return None, None, None, None
    
    # Берем первый товар
    product = product_blocks[0]
    
    # Извлечение цены
    price_block = product.find('div', class_='ElementLeaf_elementPrice__N_uvA')
    price = price_block.text.strip() if price_block else 'Unknown'

    # Извлечение информации о наличии
    in_stock = True  # Предполагаем, что товар в наличии по умолчанию
    if product.find('div', class_='OutOfStock_text__L_ZJH'):
        in_stock = False  # Если есть блок с классом "OutOfStock", то товара нет в наличии

    # Извлечение ссылки на изображение
    image_block = product.find('img', class_='ElementImage_listing__SOAed')
    image_url = image_block['src'] if image_block else 'Image not found'

    return search_url, price, in_stock, image_url