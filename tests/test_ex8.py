from ex8 import *
import pytest

def test_positivos():
    arquivo = Arquivo(10)
    assert arquivo.tamanho_total() == 10

def test_negativo():
    with pytest.raises(ValueError):
        arquivo = Arquivo(-1)