def print_info(item_id, lego_result, toypro_result):
    print(f"Search result by ID {item_id}")

    # Проверка на наличие данных от Toypro
    if toypro_result:
        print("\nResult from Toypro")

        # Проверка и вывод альтернативных ID
        if 'alt_ids' in toypro_result and len(toypro_result['alt_ids']) > 0:
            print(f"This LEGO piece has other element IDs: {toypro_result['alt_ids']}")
        else:
            print("No alternative IDs found.")
        
        # Вывод изображения и ссылки
        print(f"Image: {toypro_result.get('image_url', 'No image available')}")
        print(f"Search link: {toypro_result.get('search_url', 'No search link available')}")

        # Проверка наличия на складе
        if 'count_in_stock' in toypro_result and toypro_result['count_in_stock'] > 0:
            print(f"In stock. Count in stock: {toypro_result['count_in_stock']}")
        else:
            print("Not in stock")

        # Вывод цены и цвета
        print(f"Price: {toypro_result.get('price', 'No price available')}")
        print(f"Color: {toypro_result.get('color', 'No color information')}")
    
    else:
        print("\nNo results from Toypro")

    # Проверка на наличие данных от LEGO
    if lego_result:
        print("\nResult from LEGO")

        # Вывод изображения и ссылки
        print(f"Image: {lego_result.get('image_url', 'No image available')}")
        print(f"Search link: {lego_result.get('scearch_url', 'No search link available')}")

        # Проверка наличия на складе
        if lego_result.get('in_stock', False):
            print("In stock.")
        else:
            print("Not in stock")

        # Вывод цены
        print(f"Price: {lego_result.get('price', 'No price available')}")

    else:
        print("\nNo results from LEGO")
