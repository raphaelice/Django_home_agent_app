from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from core.models import House

class IndexView(ListView):
    model = House
    template_name = 'core/index.html'

class DetailView(DetailView):
    model = House
    template_name = 'core/detail.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'