import asyncio
from typing import Dict, Union, Optional

from toypro.search_item_toypro import search_on_toypro
from lego.search_item_lego import search_on_lego
from print_results import print_info

ResultType = Dict[str, Union[str, int, float, bool, None]]

async def fetch_lego_info(item_id: int) -> ResultType:
    return await search_on_lego(item_id)

async def fetch_toypro_info(item_id: int) -> ResultType:
    return await search_on_toypro(item_id)



def is_find_something(result_dict: ResultType, source: str) -> ResultType:
    # source: либо 'lego', либо 'toypro', чтобы добавить нужный ключ
    find_key = f"find_something_{source}"

    # Если в словаре только один элемент или is_design_id_lego/is_design_id_toypro == True
    if len(result_dict) > 1:
        result_dict[find_key] = True
    else:
        result_dict[find_key] = False
    
    return result_dict


async def main() -> ResultType:
    while True:
        try:
            item_id = int(input("Введите ID детали: ").strip())
            break
        except ValueError:
            print("Некорректный ID")

    # Параллельный запуск асинхронных запросов
    lego_task = asyncio.create_task(fetch_lego_info(item_id))
    toypro_task = asyncio.create_task(fetch_toypro_info(item_id))

    lego_result, toypro_result = await asyncio.gather(lego_task, toypro_task)
    lego_result = is_find_something(lego_result, 'lego')
    toypro_result = is_find_something(toypro_result, 'toypro')

    merged_results: ResultType = {**lego_result, **toypro_result}
    merged_results["search_id"] = item_id

    if merged_results.get("find_something_toypro") or merged_results.get("find_something_lego"):
        merged_results["alt_search_bricklink"] = f"https://www.bricklink.com/v2/search.page?q={item_id}#T=A"
        merged_results["alt_search_brickowl"] = f"https://www.brickowl.com/search/catalog?query={item_id}"
        merged_results["alt_search_constructors"] = f"https://constructors.com.ua/ua/pick-brick?text={item_id}"
        merged_results["alt_search_ebricks"] = f"https://ebricks.ru/products/search?sort=0&balance=&categoryId=&min_cost=&max_cost=&page=1&text={item_id}"
        
    return merged_results

# Запуск программы
if __name__ == "__main__":
    result_search: ResultType = asyncio.run(main())
    print_info(result_search)