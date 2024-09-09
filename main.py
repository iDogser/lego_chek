from toypro.search_item_toypro import search_item_toypro
from lego.search_item_lego import search_item_lego
from toypro.get_detail_about_item import check_item_id
from toypro.get_link_and_check_in_stock import *

def print_res_toypro(item_id, item_ids, price, color, in_stock, count_in_stock, full_link):
    print("\nSearch on https://www.toypro.com/ca")
    print(f"Item ID: {item_id}")
    if len(item_ids) > 1:
        item_ids.remove(item_id)
        print(f"Other id(s) for this item: {', '.join(map(str, item_ids))} (If the item is not found or not of stock - try this ID)")
    print(f"Price in CAD: {price}")
    print(f"Color: {color}")
    if in_stock:
        print(f"In stock. Count in stock: {count_in_stock}")
    else:
        print("Not in stock.")
    print(f"Item link: {full_link}")


def print_res_lego(item_id, price, in_stock, full_link):
    print("\nSearch on https://www.lego.com/en-us/pick-and-build/pick-a-brick")
    print(f"Item ID: {item_id}")
    print(f"Price in USD: {price}")
    if in_stock:
        print(f"In stock.")
    else:
        print("Not in stock.")
    print(f"Item link: {full_link}")


def main():
    item_id = input("Введите ID детали: ")
    item_id = item_id.strip()
    
    product_blocks_toypro = search_item_toypro(item_id)
    lego_price, lego_in_stock, lego_full_link = search_item_lego(item_id)


    if product_blocks_toypro:
        for block in product_blocks_toypro:
            print(block)
            full_link = get_product_link(block)
            item_ids, price, color, count_in_stock = check_item_id(full_link)
            if item_id in item_ids:
                in_stock = check_in_stock(block)
                print_res_toypro(item_id, item_ids, price, color, in_stock, count_in_stock, full_link)

    else:
        print(f"Блоков с ID {item_id} не найдено.")
        return
    
    
    print_res_lego(lego_price, lego_in_stock, lego_full_link)
    
   



# Запуск программы
if __name__ == "__main__":
    main()
