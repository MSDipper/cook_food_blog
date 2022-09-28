from django.urls import path
from about.views import AboutListView


urlpatterns = [
    path('', AboutListView.as_view(), name='about')
]
