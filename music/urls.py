from django.urls import path
from .import views

urlpatterns = [
    #music
    path('music', views.index, name = 'index'),

    #music/id
    path('music/<int:album_id>/', views.detail, name='detail'),

]
