from django.urls import path, include
from . import views
from .views import WidgetList
urlpatterns = [
    path('', WidgetList.as_view()),
    path('add_widget/', views.add_widget, name='add_widget'),
]