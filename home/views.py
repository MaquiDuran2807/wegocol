from django.shortcuts import render

from .models import ModelHome


from django.views.generic import ListView
# Create your views here.


class home(ListView):
    template_name = 'index.html'
    model = ModelHome
    context_object_name = 'index'

