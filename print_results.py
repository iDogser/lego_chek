def print_info(item_id, other_item_ids, price, color, in_stock, count_in_stock, full_link, image_url, search_source):
    print(f"\nSearch on {search_source}")
    if price is not None and full_link is not None and image_url is not None:
        print(f"Item ID: {item_id}")
        if other_item_ids is not None:
            if len(other_item_ids) >= 1:
                print(f"Other id(s) for this item: {', '.join(map(str, other_item_ids))} (If the item is not found or not of stock - try this ID)")
        print(f"Price in USD: {price}")
        print("Color: unknown" if color is None else f"Color: {color}")
        if in_stock:
            print(f"Count in stock: {count_in_stock}" if count_in_stock is not None else "In stock")
        else:
            print("Not in stock.")
        print(f"Item link: {full_link}")
        print(f"Image url: {image_url}")
    else:
        print("No results")
