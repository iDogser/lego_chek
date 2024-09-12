from toypro.search_item_toypro import search_item_toypro
from lego.search_item_lego import search_and_extract_product_info
from toypro.get_detail_about_item import check_item_id, get_product_block
from toypro.get_link_and_check_in_stock import check_in_stock, check_lego_design_id, get_product_link
from print_results import print_info


def process_toypro_item(item_id):
    """
    Процесс поиска на сайте ToyPro и возвращение информации.
    """
    search_list = search_item_toypro(item_id)
    if not search_list:
        print_info(None, None, None, None, None, None, None, None, 'https://www.toypro.com')
        return None, None, True

    full_link = get_product_link(search_list[0])
    product_block, is_sticker = get_product_block(full_link)
    if check_lego_design_id(product_block, item_id):
        print("You input Lego Design ID")
        print_info(None, None, None, None, None, None, None, None, 'https://www.toypro.com')
        return None, None, False
    elif is_sticker:
        print("It's a sticker")
        print_info(None, None, None, None, None, None, None, None, 'https://www.toypro.com')
        return None, None, False

    for block in search_list:
        in_stock = check_in_stock(block)
        item_ids, price, color, count_in_stock, image_url = check_item_id(product_block)
        print_info(item_id, item_ids, price, color, in_stock, count_in_stock, full_link, image_url, 'https://www.toypro.com')
        return item_ids, color, True


def process_lego_item(item_id, color):
    """
    Процесс поиска на сайте Lego и вывод информации.
    """
    lego_full_link, lego_price, lego_in_stock, lego_image_url = search_and_extract_product_info(item_id)
    print_info(item_id, None, lego_price, color, lego_in_stock, None, lego_full_link, lego_image_url, 'https://www.lego.com')


def handle_alternative_ids(item_ids):
    """
    Обработка альтернативных ID.
    """
    if item_ids and item_ids != '-':
        for alt_id in item_ids:
            print(f"\n\nSearch by alternative ID {alt_id}\n\n")
            item_ids, color, cont_find = process_toypro_item(alt_id)
            if cont_find:
                process_lego_item(alt_id, color)


def main():
    item_id = int(input("Введите ID детали: ").strip())

    item_ids, color, cont_find = process_toypro_item(item_id)
    if cont_find:
        process_lego_item(item_id, color)
        if item_ids and len(item_ids) > 1:
            item_ids.remove(item_id)
            handle_alternative_ids(item_ids)


if __name__ == "__main__":
    main()
