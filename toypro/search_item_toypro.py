import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict, Union, Optional

ResultType = Dict[str, Union[str, int, float, bool, None]]


# Асинхронный запрос к toypro
async def req_to_toypro(url: str) -> Optional[BeautifulSoup]:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                html = await response.text()
                return BeautifulSoup(html, 'html.parser')
    except aiohttp.ClientError as e:
        print(f"Ошибка запроса: {e}")
        return None
    

# Извлечение ссылок с товаров на странице
def extract_links_from_blocks(page_code_process_toypro: BeautifulSoup) -> List[str]:
    product_blocks = page_code_process_toypro.find_all('div', class_='col-12 col-sm-6 col-lg-3')
    pagination_block = page_code_process_toypro.find('div', class_='row justify-content-end')
    pagination_position = pagination_block if pagination_block else None
    
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
    

# Проверка на совпадение Design ID
def is_design_id(page_code: BeautifulSoup, item_id: int) -> bool:
    li_elements = page_code.find_all('li')
    for li in li_elements:
        if 'LEGO® Design ID:' in li.text:
            design_id = li.text.split('LEGO® Design ID:')[-1].strip()
            try:
                design_id = int(design_id)
                if item_id == design_id:
                    return True
            except ValueError:
                return False
    return False

def get_item_info_toypro(item_page: BeautifulSoup, item_id: int) -> ResultType:
    element_id_block = item_page.find_all('li')
    element_ids = []
    for li in element_id_block:
        if 'LEGO® Element ID:' in li.text:
            element_ids_text = li.text.split('LEGO® Element ID:')[-1].strip()
            element_ids = [int(id.strip()) for id in element_ids_text.split(',') if id.strip().isdigit()]
    
    if item_id in element_ids:
        price_block = item_page.find('div', class_='c_product-top__price')
        price = price_block.text.strip().split()[0] if price_block else 'Цена не найдена'

        design_id_block = item_page.find('li', text=lambda t: t and 'Design ID:' in t)
        design_id = design_id_block.text.split(':')[-1].strip() if design_id_block else None

        try:
            item_name = item_page.find('h1', class_='c_title c_title--size-2 c_product-top__title').text.strip()
        except AttributeError:
            item_name = "-"

        stock_block = item_page.find('div', class_='c_product-top__stock--indicator')
        if stock_block:
            stock_text = stock_block.text.strip()
            try:
                count_in_stock = int(stock_text.split()[1])
            except ValueError:
                count_in_stock = 0
        else:
            count_in_stock = 0

        color_block = item_page.find('li', text=lambda t: t and 'Color:' in t)
        color = color_block.text.split(':')[-1].strip() if color_block else None

        img_element = item_page.find('img', class_='c_product-top__image')
        image_url = img_element['src'] if img_element else "-"

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



# Обработка информации о товаре
async def process_item_info_toypro(links_list_toypro: List[str], item_id: int) -> ResultType:
    filtred_pages = []
    for link in links_list_toypro:
        page_code_item_toypro = await req_to_toypro(link)
        if page_code_item_toypro:
            desing_id = is_design_id(page_code_item_toypro, item_id)
            if not desing_id:
                filtred_pages.append((link, page_code_item_toypro))

    if len(filtred_pages) >= 1:
        for url, page in filtred_pages:
            item_info_toypro = get_item_info_toypro(page, item_id)
            if item_info_toypro and item_id in item_info_toypro["alt_ids"]:
                item_info_toypro["alt_ids"].remove(item_id)
                item_info_toypro["search_url_toypro"] = url
                item_info_toypro["is_design_id_toypro"] = False
                return item_info_toypro
        return {"is_design_id_toypro": True}
    else:
        return {"is_design_id_toypro": False}

# Асинхронный поиск товара на toypro
async def search_on_toypro(item_id: int) -> ResultType:
    toypro_url = f"https://www.toypro.com/us/search?search={item_id}&sortby=relevance"
    page_code_toypro = await req_to_toypro(toypro_url)
    if page_code_toypro:
        links_items_toypro = extract_links_from_blocks(page_code_toypro)
        item_info = await process_item_info_toypro(links_items_toypro, item_id)
        return item_info
    return {}





