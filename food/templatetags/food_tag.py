from django import template
from django.db.models import Count
from food.models import Category, Food

register = template.Library()


@register.inclusion_tag('food/include/tags/categories_all_photo_tag.html')
def get_categories_photo(count):
    category_list = Category.objects.order_by('id')[:count]
    return {'category_list':category_list}




@register.inclusion_tag('food/include/tags/category_tag.html')
def get_categories():
    categories = Category.objects.annotate(category_count=Count('food')).all()
    return {'categories':categories}