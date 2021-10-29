from django.shortcuts import render
from django.shortcuts import render, redirect
from main_app.models import Widget
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect 

def home(request):
    widgets = Widget.objects.all()
    return render (request, 'home.html',
    {'widgets': widgets})

class WidgetCreate(CreateView):
    model = Widget
    fields = ['description', 'quantity']
    success_url = ''

class WidgetDelete(DeleteView):
    model = Widget
    success_url = ''








#def widget_form(request):

# Create your views here.

