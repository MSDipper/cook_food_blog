from django import template
from food.models import Food, Category
from about.models import About
from django.db.models import Count



register = template.Library()



@register.simple_tag()
def get_food_posts(count=2):
    return Food.objects.order_by('id')[:count].select_related('category')


@register.simple_tag()
def get_about():
    return About.objects.all()

@register.simple_tag()
def get_categories_count():
   return Category.objects.annotate(category_count=Count('food')).all()
     