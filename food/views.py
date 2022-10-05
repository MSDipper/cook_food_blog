from django.shortcuts import render, redirect
from food.models import Food
from django.views.generic import ListView, DetailView
from food.forms import CommentForm
from django.views import View


class FoodListView(ListView):
    ''' List of dishes '''
    paginate_by = 3
    model = Food
    
    def get_queryset(self):
        return Food.objects.all()



class FoodDetailView(DetailView):
    model = Food
    context_object_name = 'food'
    slug_url_kwarg = 'slug'



class Search(ListView):
    paginate_by = 3
    
    def get_queryset(self):
        return Food.objects.filter(title__icontains=self.request.GET.get("q"))
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class GetCategoryListView(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Food.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')

class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Food.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())