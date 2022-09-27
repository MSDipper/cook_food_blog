from django.shortcuts import render
from food.models import Food
from django.views.generic import ListView, DetailView


class FoodListView(ListView):
    ''' List of dishes '''
    paginate_by = 3
    model = Food
    



class FoodDetailView(DetailView):
    model = Food
    context_object_name = 'food'


class Search(ListView):
    paginate_by = 3
    def get_queryset(self):
        return Food.objects.filter(title__icontains=self.request.GET.get("q"))
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context