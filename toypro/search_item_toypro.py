import requests
from bs4 import BeautifulSoup

def search_item_toypro(item_id):
    search_url = f"https://www.toypro.com/us/search?search={item_id}&sortby=relevance"
    
    try:
        # Выполняем запрос на страницу
        response = requests.get(search_url)
        response.raise_for_status()  # Проверка на успешный ответ
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    
    # Парсим HTML-ответ
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Поиск всех блоков с товарами
    product_blocks = soup.find_all('div', class_='col-12 col-sm-6 col-lg-3')
    
    matching_blocks = []
    for block in product_blocks:
        # Поиск по элементу, содержащему ID детали
        title_block = block.find('span', class_='c_title__secondtitle')
        if title_block:
            matching_blocks.append(block)

    if not matching_blocks:
        return None
    
    return matching_blocks



