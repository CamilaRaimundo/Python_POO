from ex2 import *
import pytest

def test_item_qtd_invalida():
    with pytest.raises(ValueError):
        Item("Livro", 20, 0)   # quantidade zero inválida

def test_item_preco_invalido():
    with pytest.raises(ValueError):
        Item("Livro", -5, 2)   # preço negativo inválido

def test_adicionar_item_valido():
    carrinho = Carrinho()
    item = Item("Livro", 10, 3)
    carrinho.adicionar(item)
    assert carrinho.total() == 30
