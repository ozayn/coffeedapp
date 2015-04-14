from django.shortcuts import render

from django.views.generic import TemplateView
#from django.views.generic.base import TemplateView

class LandingView(TemplateView):
	template_name = 'base/index.html'