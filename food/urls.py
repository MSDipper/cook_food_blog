from urllib.parse import urlparse
from django.urls import path

from food.views import FoodListView

urlpatterns = [
    path('', FoodListView.as_view(), name='food_list')
]
