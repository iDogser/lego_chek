from django.urls import path
from .views import search_item

urlpatterns = [
    path('search/', search_item),
]
