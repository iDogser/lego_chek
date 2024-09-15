import requests
from bs4 import BeautifulSoup


def req_to_lego(url):
    try:
        # Выполняем запрос на страницу
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

    # Парсим HTML-ответ
    page_code_result_lego = BeautifulSoup(response.text, 'html.parser')
    return(page_code_result_lego)

def find_item_blocks_lego(page_code_process_lego, item_id: int):
    # Получаем все блоки с товарами
    filtred_blocks_lego = []
    all_product_blocks_lego = page_code_process_lego.find_all('li', class_='ElementsList_leaf__3tVNf ElementsList_row-count-4__HKOE5')
    
    for block in all_product_blocks_lego:
        # Находим элемент, содержащий ID
        element_id_block = block.find('p', class_='ElementLeaf_elementId__Ivgn4 ds-body-xs-regular')
        
        if element_id_block:
            # Получаем текст и разбиваем по символу "/"
            ids = element_id_block.text.split('ID:')[-1].strip().split('/')
            try:
                design_id = int(ids[1])
                if item_id == design_id:
                    print("Its design_id")
                    return filtred_blocks_lego
            except:
                print("Error process design_id")

            try:
                element_id = int(ids[0])
                if item_id == element_id:
                    filtred_blocks_lego.append(block)
                    return(filtred_blocks_lego)
            except:
                print("Error process element ID")

    return(filtred_blocks_lego)

def get_item_info_lego(block_lego):
    price_block_lego = block_lego.find('div', class_='ElementLeaf_elementPrice__N_uvA')
    price_lego = price_block_lego.text.strip() if price_block_lego else 'Unknown'

    # Извлечение информации о наличии
    in_stock_lego = not bool(block_lego.find('div', class_='OutOfStock_text__L_ZJH'))

    # Извлечение ссылки на изображение
    image_block_lego = block_lego.find('img', class_='ElementImage_listing__SOAed')
    image_url_lego = image_block_lego['src'] if image_block_lego else 'Image not found'
    return {
        "price": price_lego,
        "in_stock": in_stock_lego,
        "image_url": image_url_lego
    }

def search_on_lego(item_id):
    lego_url = f"https://www.lego.com/en-us/pick-and-build/pick-a-brick?includeOutOfStock=true&query={item_id}&perPage=20"
    page_code_lego = req_to_lego(lego_url)
    item_blocks_list = find_item_blocks_lego(page_code_lego, item_id)
    if len(item_blocks_list) >= 1:
        item_info_lego = get_item_info_lego(item_blocks_list[0])
        item_info_lego["scearch_url"] = lego_url
        return item_info_lego
    else:
        return {}
