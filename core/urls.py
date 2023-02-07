from django.urls import path

from .views import HomeView, cadastro

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastro', cadastro, name='cadastro')
]