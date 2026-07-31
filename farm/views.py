from django.shortcuts import render
from django.views.generic import ListView
from .models import Farm
# Create your views here.

class FarmListView(ListView):
    model=Farm
    template_name="farm/farm_list.html"
    context_object_name='farms'
