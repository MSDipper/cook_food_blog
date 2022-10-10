
from django.shortcuts import render
from food.models import Food
from django.views.generic import ListView





class LifeStyleDetailView(ListView):
    model = Food
    paginate_by = 3
    template_name = 'lifestyle/lifestyle_list.html'
    
    def get_queryset(self):
        return Food.objects.all().select_related('category')
