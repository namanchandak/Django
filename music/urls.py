from django.urls import path
from .import views

urlpatterns = [
    path('music', views.index, name = 'index'),
]
