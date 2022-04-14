from django.shortcuts import render
from django.views.generic import DetailView, ListView
from core.models import House

class IndexView(ListView):
    model = House
    template_name = ''

class DetailView(DetailView):
    model = House
    template_name = ''