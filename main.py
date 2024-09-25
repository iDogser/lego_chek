from toypro.search_item_toypro import search_on_toypro
from lego.search_item_lego import search_on_lego
from print_results import print_info
import asyncio


def main():
    while True:
        try:
            item_id = int(input("Введите ID детали: ").strip())
            break
        except:
            print("Incorect ID")
    lego_result = search_on_lego(item_id)
    toypro_result = search_on_toypro(item_id)
    merged_results = lego_result | toypro_result
    merged_results["search_id"] = item_id
    if not merged_results["is_design_id_toypro"] or not merged_results["is_design_id_lego"]:
        merged_results["alt_search_bricklink"] = f"https://www.bricklink.com/v2/search.page?q={item_id}#T=A"
        merged_results["alt_search_brickowl"] = f"https://www.brickowl.com/search/catalog?query={item_id}"
        merged_results["alt_search_constructors"] = f"https://constructors.com.ua/ua/pick-brick?text={item_id}"
        merged_results["alt_search_ebricks"] = f"https://ebricks.ru/products/search?sort=0&balance=&categoryId=&min_cost=&max_cost=&page=1&text={item_id}"
        return merged_results
    else:
        return merged_results




if __name__ == "__main__":
    result_search = main()
    print_info(result_search)
