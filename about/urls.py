from django.urls import path
from about.views import AboutListView
from django.views.decorators.cache import  cache_page


urlpatterns = [
    path('', cache_page(60 * 15)(AboutListView.as_view()), name='about'),
    # path('', AboutListView.as_view(), name='about')
]
