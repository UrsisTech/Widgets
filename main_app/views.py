from django.shortcuts import render
from django.shortcuts import render, redirect
from models import Widget
from forms import WidgetForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView

def home(request):
    return render (request, 'home.html')
    form = WidgetForm(request.POST)
    new_widget = form.save()

class WidgetList(ListView):
    model = Widget
    context_object_name = 'widgets'







#def widget_form(request):

# Create your views here.

