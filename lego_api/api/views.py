from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import asyncio
from main import main

# Храните API-ключ в конфигурации или переменной окружения
API_KEY = 'your_api_key_here'

# Декоратор API запроса с проверкой API ключа
@api_view(['GET'])
def get_item_info(request):
    # Получаем API-ключ из заголовков запроса
    api_key = request.headers.get('API-Key')
    if api_key != API_KEY:
        return Response({"error": "Invalid API Key"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # Получаем item_id из параметров запроса
    item_id = request.query_params.get('item_id')
    if not item_id:
        return Response({"error": "Item ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        item_id = int(item_id)
    except ValueError:
        return Response({"error": "Item ID must be an integer"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Асинхронно выполняем основную логику
    result_search = asyncio.run(main(item_id))

    # Возвращаем результат
    return Response(result_search, status=status.HTTP_200_OK)
