from django.shortcuts import render
from foods.models import Food
from django.views.generic import ListView


class FoodListView(ListView):
    ''' List of dishes '''
    model = Food