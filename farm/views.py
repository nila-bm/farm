from django.shortcuts import render
from django.views.generic import DetailView,TemplateView,ListView
from .models import Farm
# Create your views here.

class FarmHome(TemplateView):
    template_name="farm/home.html"

class FarmListView(ListView):
    model=Farm
    template_name="farm/farm_list.html"
    context_object_name='farms'

class FarmDetailView(DetailView):
    model=Farm
    template_name="farm/farm_detail.html"
    context_object_name='farm'

