from toypro.search_item_toypro import search_on_toypro
from lego.search_item_lego import search_on_lego
from print_results import print_info
import asyncio


def main():
    item_id = int(input("Введите ID детали: ").strip())
    lego_result = search_on_lego(item_id)
    toypro_result = search_on_toypro(item_id)

    print_info(item_id, lego_result, toypro_result)



if __name__ == "__main__":
    main()


# async def main():
#     item_id = int(input("Введите ID детали: ").strip())
    
#     # Асинхронный запуск обеих функций
#     lego_task = asyncio.create_task(search_on_lego(item_id))
#     toypro_task = asyncio.create_task(search_on_toypro(item_id))
    
#     # Ожидание завершения обеих задач
#     lego_result = await lego_task
#     toypro_result = await toypro_task
    
#     # Вызов функции для печати информации
#     print_info(item_id, lego_result, toypro_result)

# # Запуск программы через asyncio.run()
# if __name__ == "__main__":
#     asyncio.run(main())
