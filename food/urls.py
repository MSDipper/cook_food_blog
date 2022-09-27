from urllib.parse import urlparse
from django.urls import path

from food.views import FoodListView, FoodDetailView, Search

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    path('<slug:slug>/', FoodDetailView.as_view(), name='food_single'),
    path('', FoodListView.as_view(), name='food_list')
]
