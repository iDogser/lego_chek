import requests
from bs4 import BeautifulSoup

def search_item_lego(item_id):
    search_url = f"https://www.lego.com/en-us/pick-and-build/pick-a-brick?query={item_id}"
    
    # Выполняем запрос на страницу
    response = requests.get(search_url)
    if response.status_code != 200:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        return None
    
    # Парсим HTML-ответ
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим блок с информацией о товаре
    product_block = soup.find('li', class_='ElementsList_leaf__3tVNf ElementsList_row-count-4__HKOE5')
    print(product_block)
    # Если продукт не найден
    if not product_block:
        print("Товар не найден")
        return None
    
    # Извлечение цены
    price_block = product_block.find('div', class_='ElementLeaf_elementPrice__N_uvA')
    price = price_block.text.strip() if price_block else 'Цена не найдена'

    # Извлечение информации о наличии
    in_stock = True  # Предполагаем, что товар в наличии по умолчанию
    if product_block.find('div', class_='OutOfStock_text__L_ZJH'):
        in_stock = False  # Если есть блок с классом "OutOfStock", то товара нет в наличии
    
    # Возвращаем цену и информацию о наличии
    # return price, in_stock, search_url
    print(price, in_stock, search_url)


if __name__ == "__main__":
    search_item_lego(6013530)