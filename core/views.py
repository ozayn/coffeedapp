from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
import core.models as coremodels

class LandingView(TemplateView):
    template_name = 'base/index.html'


class LocationListView(ListView):
	model = coremodels.Location
	template_name = 'location/list.html'


# class LocationListView(ListView):
# 	model = coremodels.Location
# 	template_name = 'base/theme.html'