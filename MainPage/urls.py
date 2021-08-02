from os import name
from django.urls import path
from . import views 

urlpatterns=[
    path('',views.index, name='index'),
    path('predictHD',views.predictHD, name="predictHD"),
    path('Type', views.Type, name='Type'),
    path('Prevention', views.Prevention, name="Prevention"),
    path('Symptoms', views.Symptoms, name="Symptoms"),
    path('Treatment', views.Treatment, name="Treatment"),
    path('Causes', views.Causes, name="Causes"),
    # path('index',views.index, name='index'),
]