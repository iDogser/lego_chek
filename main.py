from toypro.search_item_toypro import search_item_toypro
from lego.search_item_lego import *
from toypro.get_detail_about_item import *
from toypro.get_link_and_check_in_stock import *

def print_res_toypro(item_id, item_ids, price, lego_color, color, in_stock, count_in_stock, full_link, image_url):
    print("\nSearch on https://www.toypro.com/ca")
    print(f"Item ID: {item_id}")
    if len(item_ids) > 1:
        item_ids.remove(item_id)
        print(f"Other id(s) for this item: {', '.join(map(str, item_ids))} (If the item is not found or not of stock - try this ID)")
    else:
        print("Other id(s) for this item: -")
    print(f"Price in CAD: {price}")
    print(f"Lego color: {lego_color}")
    print(f"Color: {color}")
    if in_stock:
        print(f"In stock. Count in stock: {count_in_stock}")
    else:
        print("Not in stock.")
    print(f"Item link: {full_link}")
    print(f"Image url: {image_url}")
    


def print_res_lego(item_id, price, lego_color, color, in_stock, full_link, lego_image_url):
    print("\nSearch on https://www.lego.com/en-us/pick-and-build/pick-a-brick")
    print(f"Item ID: {item_id}")
    print(f"Price in USD: {price}")
    print(f"Lego color: {lego_color}")
    print(f"Color: {color}")
    if in_stock:
        print(f"In stock.")
    else:
        print("Not in stock.")
    print(f"Item link: {full_link}")
    print(f"Image url: {lego_image_url}")

def main():
    item_id = input("Введите ID детали: ")
    item_id = item_id.strip()
    
    search_list = search_item_toypro(item_id)
    if search_list:
        full_link = get_product_link(search_list[0])
        product_block, is_sticker = get_product_block(full_link)
        is_lego_design_id = check_lego_design_id(product_block, item_id)
        if is_lego_design_id:
            print("You input Lego Design ID")
            return
        elif is_sticker:
            print("It's a stickers")
            return
        else:
            for block in search_list:
                in_stock = check_in_stock(block)
                item_ids, price, color, lego_color, count_in_stock, image_url = check_item_id(product_block)
                if lego_color is None and color is None:
                    print(f"No items with ID {item_id} were found")
                    return
                else:
                    print_res_toypro(item_id, item_ids, price, lego_color, color, in_stock, count_in_stock, full_link, image_url)
                    break
    else:
        print(f"No items with ID {item_id} were found")
    


    
    lego_full_link, lego_price, lego_in_stock, lego_image_url = search_and_extract_product_info(item_id)
    print_res_lego(item_id, lego_price, lego_color, color, lego_in_stock, lego_full_link, lego_image_url)
    
   



# Запуск программы
if __name__ == "__main__":
    main()
