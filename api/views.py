from django.http import JsonResponse
import asyncio

# API ключ, который мы будем проверять
API_KEY = '73904a9c-74a7-4643-b483-e1b10c3f287d'

def api_key_required(view_func):
    def wrapper(request, *args, **kwargs):
        api_key = request.GET.get('api_key')
        if api_key != API_KEY:
            return JsonResponse({'error': 'Invalid API key'}, status=403)
        return view_func(request, *args, **kwargs)
    return wrapper

@api_key_required
def search_item(request):
    item_id = request.GET.get('item_id')
    
    if not item_id:
        return JsonResponse({'error': 'Item ID is required'}, status=400)
    
    # Логика для поиска детали по item_id через main.py
    from main import main  # Импорт асинхронной функции из вашего скрипта main.py
    try:
        # Если main - асинхронная функция, нужно вызвать ее через asyncio.run()
        result_search = asyncio.run(main(int(item_id)))  # Приводим item_id к int
    except ValueError:
        return JsonResponse({'error': 'Invalid Item ID'}, status=400)
    
    return JsonResponse(result_search, safe=False)  # safe=False, если result_search не dict
