from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('dados-recebidos', views.api, name='api'),
]