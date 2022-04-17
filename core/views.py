from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from core.models import House, Location

class IndexView(View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        queryset = House.objects.all()
        style_query = request.GET.get('style-query')
        location_query = request.GET.get('location-query')
        price_query = request.GET.get('price-query')
        water_query = request.GET.get('water-query')
        occupied_query = request.GET.get('occupied-query')

        if style_query is not None and style_query.strip() != '':
            queryset = queryset.filter(style=style_query)
        
        if location_query is not None and location_query.strip() != '':
            queryset = queryset.filter(location=location_query)

        if price_query is not None and price_query.strip() != '':
            queryset = queryset.filter(price__lte=price_query)

        if water_query is not None:
            queryset = queryset.filter(water=True)

        if occupied_query is not None:
            queryset = queryset.filter(occupied=True)

        context = {
            'location': Location.objects.all(),
            'queryset': queryset,
            'styles': House.STYLE 
        }
        return render(request, self.template_name, context)

class DetailView(DetailView):
    model = House
    template_name = 'core/detail.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'