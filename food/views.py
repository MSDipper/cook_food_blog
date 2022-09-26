from django.shortcuts import render
from food.models import Food
from django.views.generic import ListView, DetailView


class FoodListView(ListView):
    ''' List of dishes '''
    paginate_by = 3
    model = Food
    



class FoodDetailView(DetailView):
    model = Food