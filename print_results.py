def print_info(result_dict):
    print(f"Search result by ID {result_dict["search_id"]}")

    # Проверка на наличие данных от Toypro
    if not result_dict["is_design_id_toypro"]:
        print("\nResult from Toypro")
        print(f"Item name: {result_dict['item_name_toypro']}")
        print(f"LEGO Design ID: {result_dict['design_id_toypro']}")
        # Проверка и вывод альтернативных ID
        if len(result_dict['alt_ids']) > 0:
            print(f"This LEGO piece has other element IDs: {result_dict['alt_ids']}")
        else:
            print("No alternative IDs found.")
        
        # Вывод изображения и ссылки
        print(f"Image URL: {result_dict["image_url_toypro"]}")
        print(f"Search link: {result_dict["search_url_toypro"]}")

        # Проверка наличия на складе
        if result_dict['in_stock_toypro'] > 0:
            print(f"In stock. Count in stock: {result_dict['in_stock_toypro']}")
        else:
            print("Not in stock")

        # Вывод цены и цвета
        print(f"Price: {result_dict["price_toypro"]}")
        print(f"Color: {result_dict["color"]}")
    
    else:
        print("\nNo results from Toypro")

    # Проверка на наличие данных от LEGO
    if not result_dict["is_design_id_lego"]:
        print("\nResult from LEGO")
        print(f"Item name: {result_dict['item_name_lego']}")
        print(f"LEGO Design ID: {result_dict['design_id_lego']}")
        
        # Вывод изображения и ссылки
        print(f"Image URL: {result_dict["image_url_lego"]}")
        print(f"Search link: {result_dict["scearch_url_lego"]}")

        # Проверка наличия на складе
        if result_dict['in_stock_lego']:
            print(f"In stock.")
        else:
            print("Not in stock")

        # Вывод цены и цвета
        print(f"Price: {result_dict["price_lego"]}")
    
    else:
        print("\nNo results from LEGO")

    if not result_dict["is_design_id_toypro"] or not result_dict["is_design_id_lego"]:
        print("\nElse try this links: ")
        print(f"A store where peoples from around the world sell LEGO parts:\n{result_dict["alt_search_bricklink"]}\n")
        print(f"A store where peoples from around the world sell LEGO parts:\n{result_dict["alt_search_brickowl"]}\n")
        print(f"The best store for Ukraine with fast delivery:\n{result_dict["alt_search_constructors"]}\n")
        print(f"The best store for Russia with fast delivery:\n{result_dict["alt_search_ebricks"]}\n")