from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from core.models import House, Location, Style

class IndexView(View):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        queryset = House.objects.all()
        style_query = request.GET.get('style-query')
        location_query = request.GET.get('location-query')
        price_query = request.GET.get('price-query')
        water_query = request.GET.get('water-query')
        vacancy_query = request.GET.get('vacancy-query')

        if style_query is not None and style_query.strip() != '':
            queryset = queryset.filter(style__id=style_query)
        
        if location_query is not None and location_query.strip() != '':
            queryset = queryset.filter(location=Location.objects.get(pk=location_query))

        if price_query is not None and price_query.strip() != '':
            queryset = queryset.filter(price__lte=price_query)

        if water_query is not None:
            queryset = queryset.filter(water=True)

        if vacancy_query is not None:
            queryset = queryset.filter(vacant=True)

        context = {
            'location': Location.objects.all(),
            'queryset': queryset,
            'styles': Style.objects.all(),
        }
        return render(request, self.template_name, context)

class DetailView(DetailView):
    model = House
    template_name = 'core/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        house = self.get_object()
        same_location = self.model.objects.filter(location=house.location)
        context.update({
            'same_location': same_location
        })
        return context

