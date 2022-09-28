from django.urls import path
from lifestyle.views import LifeStyleDetailView 


urlpatterns = [
    path('', LifeStyleDetailView.as_view(), name='lifestyle')
]
