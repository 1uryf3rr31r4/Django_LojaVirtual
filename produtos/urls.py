from django.urls import path
from .views import lista_produtos, adicionar_ao_carrinho, remover_do_carrinho

urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', remover_do_carrinho, name='remover_do_carrinho')
]