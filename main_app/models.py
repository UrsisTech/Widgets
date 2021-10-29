from django.db import models
from django.forms import ModelForm
from django.urls import reverse
# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def get_success_url(self):
        return reverse('some_url')
