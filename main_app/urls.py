from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.WidgetCreate.as_view(), name='widget_create'),
    path('delete/', views.WidgetDelete.as_view(), name='widget_delete'),

]