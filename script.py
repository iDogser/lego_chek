from print_results import print_info
import asyncio
from typing import Dict, Union, Optional
from main import main

ResultType = Dict[str, Union[str, int, float, bool, None]]

# Запуск программы
if __name__ == "__main__":
    while True:
        try:
            item_id = int(input("Введите ID детали: ").strip())
            break
        except ValueError:
            print("Некорректный ID")
    result_search: ResultType = asyncio.run(main(item_id))
    print_info(result_search)