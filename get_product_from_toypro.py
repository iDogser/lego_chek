# Функция для поиска блока детали по ID
import requests
from bs4 import BeautifulSoup

# Функция для поиска блока детали по ID
def search_item(item_id):
    # URL поискового запроса
    search_url = f"https://www.toypro.com/ca/search?search={item_id}"
    
    # Запрос на страницу поиска
    response = requests.get(search_url)
    if response.status_code != 200:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск всех блоков с товарами
    product_blocks = soup.find_all('div', class_='col-12 col-sm-6 col-lg-3')
    # Поиск блоков, содержащих введенный ID
    matching_blocks = []
    for block in product_blocks:
        title_block = block.find('span', class_='c_title__secondtitle')
        print(title_block)
        if title_block:  # Поиск ID в тексте блока
            matching_blocks.append(block)  # Добавляем весь блок в список
            print(block)

    # Если есть найденные блоки
    if matching_blocks:
        for block in matching_blocks:
            print(block.prettify())  # Корректный вывод блока
    else:
        print("Товар с данным ID не найден.")
    
    return matching_blocks