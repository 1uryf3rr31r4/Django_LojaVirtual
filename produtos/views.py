# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .cart import Carrinho

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = Carrinho(request)
    carrinho.adicionar(produto)
    return redirect('lista_produtos')

def remover_do_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = Carrinho(request)
    carrinho.remover(produto)
    return redirect('lista_produtos')