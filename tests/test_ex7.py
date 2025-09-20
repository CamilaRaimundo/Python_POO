from ex7 import *
import pytest

def test_positivos():
    circulo = Circulo(raio=10)
    assert circulo.area() == 314.0
    assert circulo.perimetro() == 62.800000000000004

    retangulo = Retangulo(base=10, altura=5)
    assert retangulo.area() == 50
    assert retangulo.perimetro() == 30

def test_negativos():
    with pytest.raises(ValueError):
        circulo = Circulo(raio=-10)

    with pytest.raises(ValueError):
        retangulo = Retangulo(base=-10, altura=-5)

def test_caracter():
    with pytest.raises(TypeError):
        circulo = Circulo(raio='a')

    with pytest.raises(TypeError):
        retangulo = Retangulo(base='a', altura=-5)
        retangulo = Retangulo(base=-10, altura='a')


    