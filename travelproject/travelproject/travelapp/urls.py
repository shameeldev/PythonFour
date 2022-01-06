from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo,name='demo'),
    path('html/', views.htmlrender,name='html'),
    path('about/', views.about,name='about')

]