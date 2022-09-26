from django import template

from food.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    ''' The output of categories in the food blog '''
    return Category.objects.all()