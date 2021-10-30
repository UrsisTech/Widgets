from django.forms import ModelForm, fields
from .models import Widget

class Form(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
        