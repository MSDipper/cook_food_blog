from django import template
from about.models import About

register = template.Library()


# @register.simple_tag()
# def get_about():
#     return About.objects.all()