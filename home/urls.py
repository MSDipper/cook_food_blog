from django.urls import path
from home.views import homepage
from django.views.decorators.cache import  cache_page

urlpatterns = [
    path('', cache_page(60 * 15)(homepage), name='home'),
    # path('', homepage, name='home')
]
