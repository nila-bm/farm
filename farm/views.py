from django.shortcuts import render
from django.views.generic import DetailView,TemplateView,ListView,CreateView
from .models import Farm
from .forms import FarmForm
from django.urls import reverse_lazy


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

class FarmCreateView(CreateView):
    model = Farm
    form_class = FarmForm
    template_name = 'farm/farm_create.html'
    success_url = reverse_lazy('farm:farmlist')

  