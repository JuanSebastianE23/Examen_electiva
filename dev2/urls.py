from django.urls import path
from . import views

app_name = 'dev2'

urlpatterns = [
    path('', views.hoja_vida, name='hoja-vida'),
]
