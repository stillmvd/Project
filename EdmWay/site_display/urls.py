from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('authorization/', views.authorization, name='authorization'),
    path('performers/', views.performers, name='performers'),
    path('registration/', views.registration, name='registration'),
    path('genres/', views.genres, name='genres'),
]