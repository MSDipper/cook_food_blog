from django.urls import path
from lifestyle.views import LifeStyleDetailView 
from django.views.decorators.cache import  cache_page


urlpatterns = [
    path('', cache_page(60 * 15)(LifeStyleDetailView.as_view()), name='lifestyle'),
    # path('', LifeStyleDetailView.as_view(), name='lifestyle')
]
