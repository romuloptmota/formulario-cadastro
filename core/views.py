from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ProdutoModelForms


class HomeView(TemplateView):
    template_name = 'home.html'


def cadastro(request):
    return render(request, 'cadastro.html')
