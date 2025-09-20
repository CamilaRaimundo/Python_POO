from ex6 import *
import pytest

def test_positivos():
    clt = CLT('Camila', 'Analista de Sistemas', 8000)
    assert clt.pagar() == 5600

    pj = PJ('Fabricio', 'Supervisor de TI', 210, 40)
    assert pj.pagar() == 8400

def test_negativos_salario():
    with pytest.raises(ValueError):
        clt = CLT('Camila', 'Analista de Sistemas', -2500) #o erro é capturado antes da função, ou seja, no __init__

def test_negativos_horas():
    with pytest.raises(ValueError):
        pj = PJ('Fabricio', 'Supervisor de TI', -210, 40)

def test_negativos_valor_hora():
    with pytest.raises(ValueError):
        pj = PJ('Fabricio', 'Supervisor de TI', 210, -40)

def test_caracter():
    with pytest.raises(TypeError):
        clt = CLT('Camila', 'Analista de Sistemas', 'a')
    
    with pytest.raises(TypeError):
        pj = PJ('Fabricio', 'Supervisor de TI', 'a', -40)

    with pytest.raises(TypeError):
        pj = PJ('Fabricio', 'Supervisor de TI', 210, 'a')