from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect 
from .forms import Form

def home(request):
    widgets = Widget.objects.all()
    form = Form()
    return render (request, 'home.html',
    {'widgets': widgets, 'form' : form})

def WidgetCreate(request):
    print('Form')
    form = Form(request.POST)
    if form.is_valid():
        form.save()
        print()
    return redirect('home')
    

def WidgetDelete(request, widget_id):
    
    b = Widget.objects.get(id=widget_id)
    # This will delete the Blog and all of its Entry objects.
    b.delete()
    return redirect('home')







#def widget_form(request):

# Create your views here.

