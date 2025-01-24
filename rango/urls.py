from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index2, name='index2'),
    path('about/', views.about, name='about'),
]
