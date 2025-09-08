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

def test_deposito_zero(obj1):
    with pytest.raises(ValueError):
        obj1.depositar(0)

def test_depositar_caracter(obj1):
    with pytest.raises(TypeError):
        obj1.depositar('abc')

def test_saque_invalido(obj1):
    obj1.depositar(20)
    obj1.sacar(1)
    assert obj1.saldo == 19

def test_saque_maior_que_saldo(obj1):
    obj1.depositar(10)
    with pytest.raises(ValueError):
        obj1.sacar(20)

def test_saque_tipo_invalido(obj1):
    obj1.depositar(10)
    with pytest.raises(TypeError):
        obj1.sacar("xyz")

def test_extrato(obj1):
    obj1.depositar(15)
    assert obj1.extrato() == "Seu saldo atual é de: R$15"

def test_conta_poupanca_juros():
    conta = ContaPoupanca(1, "Carlos", 1000, 0.1)
    juros, saldo = conta.aplicar_juros()
    assert juros == 100
    assert saldo == 1100

def test_conta_corrente_basica():
    conta = ContaCorrente(2, "Ana", 500)
    conta.depositar(200)
    conta.sacar(100)
    assert conta.saldo == 600
