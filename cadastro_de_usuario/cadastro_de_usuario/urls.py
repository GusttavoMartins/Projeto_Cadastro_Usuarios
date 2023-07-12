from django.urls import path
from app_cadastro_de_usuario import views

urlpatterns = [
    path('', views.home, name='home'),
]
