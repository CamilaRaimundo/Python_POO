from ex3 import * 
import pytest

def test_idade_calculada_correta():
    obj1 = Midias("Camila", 2005)
    assert obj1.idade_calculada == 20
    
def test_anos_negativos():
    with pytest.raises(ValueError):
        obj1 = Midias("Teste", 0)

def test_duracao_negativa():
    with pytest.raises(ValueError):
        obj2 = Filme("Teste2", 2001, -8)

def test_paginas_negativas():
    with pytest.raises(ValueError):
        obj3 = Livro("Teste3", 2000, -1)
    