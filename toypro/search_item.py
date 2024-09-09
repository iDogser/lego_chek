import requests
from bs4 import BeautifulSoup

def search_item(item_id):
    search_url = f"https://www.toypro.com/ca/search?search={item_id}"
    
    response = requests.get(search_url)
    print(response)
    if response.status_code != 200:
        print(f"Ошибка запроса. Код ответа: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_blocks = soup.find_all('div', class_='col-12 col-sm-6 col-lg-3')
    matching_blocks = []
    for block in product_blocks:
        title_block = block.find('span', class_='c_title__secondtitle')
        if title_block:
            matching_blocks.append(block)

    if not matching_blocks:
        print("Товар с данным ID не найден.")
        return None
    
    return matching_blocks