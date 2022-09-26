from django.shortcuts import render
from food.models import Food
from django.views.generic import ListView


class FoodListView(ListView):
    ''' List of dishes '''
    model = Food