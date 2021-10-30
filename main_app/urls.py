from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.WidgetCreate, name='widget_create'),
    path('delete/<int:widget_id>/', views.WidgetDelete, name='widget_delete'),

]