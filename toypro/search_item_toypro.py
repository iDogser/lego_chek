import requests
from bs4 import BeautifulSoup
import re


def req_to_toypro(url):
    try:
        # Выполняем запрос на страницу
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    
    # Парсим HTML-ответ
    page_code_result_toypro = BeautifulSoup(response.text, 'html.parser')
    return page_code_result_toypro

def extract_links_from_blocks(page_code_process_toypro):
    product_blocks = page_code_process_toypro.find_all('div', class_='col-12 col-sm-6 col-lg-3')
    pagination_block = page_code_process_toypro.find('div', class_='row justify-content-end')
    if pagination_block:
        pagination_position = pagination_block
    else:
        pagination_position = None
    
    links = []

    for block in product_blocks:
        if pagination_position and block.find_previous() == pagination_position:
            break
        link_element = block.find('a', class_='c_product-block__link h_stretched-link')
        if link_element and 'href' in link_element.attrs:
            link = f"https://www.toypro.com{link_element['href']}"
            if link not in links:
                links.append(link)
    return links
    

def is_design_id(page_code, item_id):
    li_elements = page_code.find_all('li')
    for li in li_elements:
        if 'LEGO® Design ID:' in li.text:
            design_id = li.text.split('LEGO® Design ID:')[-1].strip()
            try:
                design_id = int(design_id)
                if item_id == design_id:
                    return True
            except:
                return False
    return False

def get_item_info_toypro(item_page, item_id):
    
    element_id_block = item_page.find_all('li')
    element_ids = []
    for li in element_id_block:
        if 'LEGO® Element ID:' in li.text:
            element_ids_text = li.text.split('LEGO® Element ID:')[-1].strip()
            # Разделяем строку по запятым и удаляем пробелы
            element_ids = [int(id.strip()) for id in element_ids_text.split(',') if id.strip().isdigit()]
    if item_id in element_ids:
        price_block = item_page.find('div', class_='c_product-top__price')
        price = price_block.text.strip().split()[0] if price_block else 'Цена не найдена'


        # Извлечение DesignID
        design_id_block = item_page.find('li', text=lambda t: t and 'Design ID:' in t)
        design_id = design_id_block.text.split(':')[-1].strip() if design_id_block else None

        # Извлечение названия
        try:
            item_name = item_page.find('h1', class_='c_title c_title--size-2 c_product-top__title').text.strip()
        except:
            item_name = "-"

        # Извлечение количества на складе
        stock_block = item_page.find('div', class_='c_product-top__stock--indicator')
        if stock_block:
            stock_text = stock_block.text.strip()
            try:
                count_in_stock = int(stock_text.split()[1])
            except:
                count_in_stock = 0
        else:
            count_in_stock = 0

        # Обычный цвет
        color_block = item_page.find('li', text=lambda t: t and 'Color:' in t)
        color = color_block.text.split(':')[-1].strip() if color_block else None

        # Извлечение значения атрибута 'src' (ссылка на изображение)
        img_element = item_page.find('img', class_='c_product-top__image')
        if img_element:
            
            image_url = img_element['src']
        else:
            image_url = "-"
        return {
            "alt_ids": element_ids,
            "color": color,
            "item_name_toypro": item_name,
            "price_toypro": price,
            "in_stock_toypro": count_in_stock,
            "image_url_toypro": image_url,
            "design_id_toypro": design_id
        }
    else:
        return {}


def process_item_info_toypro(links_list_toypro, item_id):
    filtred_pages = []
    for link in links_list_toypro:
        page_code_item_toypro = req_to_toypro(link)
        desing_id = is_design_id(page_code_item_toypro, item_id)
        if not desing_id:
            filtred_pages.append((link, page_code_item_toypro))
    if len(filtred_pages) >= 1:
        for url, page in filtred_pages:
            item_info_toypro = get_item_info_toypro(page, item_id)
            if item_info_toypro and item_id in item_info_toypro["alt_ids"]:
                item_info_toypro["alt_ids"].remove(item_id)
                item_info_toypro["search_url_toypro"] = url
                item_info_toypro["is_design_id_toypro"] = desing_id
                return item_info_toypro
        return {"is_design_id_toypro": True}
    else:
        return {"is_design_id_toypro": True}

def search_on_toypro(item_id):
    toypro_url = f"https://www.toypro.com/us/search?search={item_id}&sortby=relevance"
    page_code_toypro = req_to_toypro(toypro_url)
    links_items_toypro = extract_links_from_blocks(page_code_toypro)
    item_info = process_item_info_toypro(links_items_toypro, item_id)
    return item_info





