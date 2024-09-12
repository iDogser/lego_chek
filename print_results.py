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
    if price is not None and full_link is not None and lego_image_url is not None:
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
    else:
        print("No results")