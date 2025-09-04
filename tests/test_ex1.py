from ex1 import *
import pytest


@pytest.fixture
def obj1():
    return Conta(123, 'Camila', 0)


def test_positivos(obj1):
    obj1.depositar(20)
    assert obj1.saldo == 20


def test_falhas_deposito_negativo(obj1):

    with pytest.raises(ValueError):
        obj1.depositar(-15)


def test_depositar_caracter(obj1):
    with pytest.raises(TypeError):
        obj1.depositar('a')


def test_saque_invalido(obj1):
    obj1.depositar(20)
    obj1.sacar(1)
    assert obj1.saldo == 19
    
    with pytest.raises(ValueError):
        obj1.sacar(20)
