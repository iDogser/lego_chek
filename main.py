from toypro.search_item_toypro import search_item_toypro
from lego.search_item_lego import search_and_extract_product_info
from toypro.get_detail_about_item import check_item_id, get_product_block
from toypro.get_link_and_check_in_stock import check_in_stock, check_lego_design_id, get_product_link
from print_results import print_res_lego, print_res_toypro

def toypro_search_logic(item_id):
    search_list = search_item_toypro(item_id)
    if search_list:
        full_link = get_product_link(search_list[0])
        product_block, is_sticker = get_product_block(full_link)
        is_lego_design_id = check_lego_design_id(product_block, item_id)
        if is_lego_design_id:
            print("You input Lego Design ID")
            return None, None, None
        elif is_sticker:
            print("It's a stickers")
            return None, None, None
        else:
            for block in search_list:
                in_stock = check_in_stock(block)
                item_ids, price, color, lego_color, count_in_stock, image_url = check_item_id(product_block)
                if lego_color is None and color is None:
                    print(f"No items with ID {item_id} were found")
                    return None, None, None
                else:
                    print_res_toypro(item_id, item_ids, price, lego_color, color, in_stock, count_in_stock, full_link, image_url)
                    return item_ids, lego_color, color
    else:
        print(f"No items with ID {item_id} were found")
        return None

def lego_search_logic(item_id, lego_color, color):
    if lego_color is not None and color is not None:
        lego_full_link, lego_price, lego_in_stock, lego_image_url = search_and_extract_product_info(item_id)
        print_res_lego(item_id, lego_price, lego_color, color, lego_in_stock, lego_full_link, lego_image_url)

def main():
    item_id = input("Введите ID детали: ")
    item_id = item_id.strip()
    
    item_ids, lego_color, color = toypro_search_logic(item_id)
    lego_search_logic(item_id, lego_color, color)
    
    if item_ids is not None and item_ids != '-':
        for id in item_ids:
            print(f"\n\nSearch by alternative ID {id}\n\n")
            item_ids, lego_color, color = toypro_search_logic(id)
            lego_search_logic(id, lego_color, color)

    
   



# Запуск программы
if __name__ == "__main__":
    main()
