from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels
#from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView

class LandingView(TemplateView):
    template_name = 'base/index.html'


class LocationListView(ListView):
	model = coremodels.Location
	template_name = 'location/list.html'


# class LocationListView(ListView):
# 	model = coremodels.Location
# 	template_name = 'base/theme.html'


class LocationDetailView(DetailView):
    model = coremodels.Location
    template_name = 'location/detail.html'
    context_object_name = 'location'
    

class LocationCreateView(CreateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields = "__all__"

class SearchListView(LocationListView):
	def get_queryset(self):
		incoming_query_string = self.request.GET.get('query', '')
		return coremodels.Location.objects.filter(title__icontains=incoming_query_string)


class LocationUpdateView(UpdateView):
	model = coremodels.Location
	template_name = 'base/form.html'
	fields = "__all__"



