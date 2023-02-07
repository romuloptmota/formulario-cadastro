from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ProdutoModelForms


class HomeView(TemplateView):
    template_name = 'home.html'


def cadastro(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForms(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForms()
        else:
            messages.error(request, 'Erro ao salvar produto')

    else:
        form = ProdutoModelForms()

    context = {
        'form': form
    }

    return render(request, 'cadastro.html', context)
