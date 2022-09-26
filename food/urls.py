from urllib.parse import urlparse
from django.urls import path

from food.views import FoodListView, FoodDetailView

urlpatterns = [
    path('<slug:slug>/', FoodDetailView.as_view(), name='food_single'),
    path('', FoodListView.as_view(), name='food_list')
]
