from django.shortcuts import render
from about.models import About
from django.views.generic import ListView


class AboutListView(ListView):
    model = About
    template_name = 'about/about_us.html'
    