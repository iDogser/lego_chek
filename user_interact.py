from get_product_from_toypro import search_item
from bs4 import BeautifulSoup

def check_in_stock(block):
    html_code = str(block)
    if "Add to Cart" in html_code:
        return True
    elif "Email notification" in html_code:
        return False
    else:
        return None
    
# Функция для получения ссылки из блока
def get_product_link(block):
    # Ищем элемент <a> с классом 'c_product-block__link h_stretched-link'
    link_element = block.find('a', class_='c_product-block__link h_stretched-link')
    
    if link_element:
        # Извлекаем значение атрибута href
        link = link_element['href']
        # Добавляем домен к относительной ссылке
        full_link = f"https://www.toypro.com{link}"
        return full_link
    return None

# Основная программа
def main():
    item_id = input("Введите ID детали: ")
    item_id = item_id.strip()
    product_blocks = search_item(item_id)
    
    if product_blocks:
        block = product_blocks[0]
        print(product_blocks[0].prettify())
        print(f"Найдено {len(product_blocks)} блоков, соответствующих ID {item_id}:")
    else:
        print(f"Блоков с ID {item_id} не найдено.")
        return

    in_stock = check_in_stock(block)
    print(in_stock)
    full_link = get_product_link(block)
    print(full_link)



# Запуск программы
if __name__ == "__main__":
    main()
