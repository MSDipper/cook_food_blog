from urllib.parse import urlparse
from django.urls import path

from food.views import FoodListView, FoodDetailView, Search, GetCategoryListView, AddComment

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    path('category/<slug:slug>/', GetCategoryListView.as_view(), name='get_category'),
    path('comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
    path('<slug:slug>/', FoodDetailView.as_view(), name='food_single'),
    path('', FoodListView.as_view(), name='food_list')
]
