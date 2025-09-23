from ex9 import *
import pytest

def test_diminuir_aumentar_estoque():
    p = Produto(101, "Notebook", 10, 3000)
    
    # Diminuir estoque
    p.diminuir_estoque(3)
    assert p.get_quantidade() == 7
    
    # Aumentar estoque
    p.aumentar_estoque(5)
    assert p.get_quantidade() == 12
    
    # Testar erro se pedir mais que disponível
    with pytest.raises(ValueError):
        p.diminuir_estoque(20)


def test_buscar_produto():
    p1 = Produto(101, "Notebook", 10, 3000)
    estoque = Estoque()
    estoque.adicionar_produto(p1)
    
    produto_encontrado = estoque.buscar_produto(101)
    assert produto_encontrado.nome == "Notebook"
    
    # Testar produto inexistente
    with pytest.raises(ValueError):
        estoque.buscar_produto(999)


def test_item_pedido():
    p = Produto(102, "Mouse", 50, 150)
    item = ItemPedido(p, 5)
    
    # Quantidade correta
    assert item.quantidade == 5
    
    # Estoque atualizado
    assert p.get_quantidade() == 45
    
    # Subtotal correto (com frete 1%)
    assert item.subtotal == pytest.approx((150*5)*1.01)
    
    # Testar erro se estoque insuficiente
    with pytest.raises(ValueError):
        ItemPedido(p, 100)

def test_pedido_com_cupom():
    p1 = Produto(101, "Notebook", 10, 3000)
    p2 = Produto(102, "Mouse", 50, 150)
    
    pedido = Pedido()
    pedido.adicionar_item(p1, 2)
    pedido.adicionar_item(p2, 5)
    
    # Total antes do cupom
    subtotal_esperado = (2*3000*1.01) + (5*150*1.01)
    assert pedido.total == pytest.approx(subtotal_esperado)
    
    # Aplicar cupom de 10%
    pedido.aplicar_cupom(0.1)
    assert pedido.total == pytest.approx(subtotal_esperado*0.9)
    
    # Testar cupom inválido
    with pytest.raises(ValueError):
        pedido.aplicar_cupom(1.5)


def test_pagamento():
    p1 = Produto(101, "Notebook", 10, 3000)
    pedido = Pedido()
    pedido.adicionar_item(p1, 1)
    
    pagamento = Pagamento("Cartão")
    resultado = pagamento.pagar(pedido)
    
    assert "Pagamento de R$" in resultado
    assert "Cartão" in resultado
