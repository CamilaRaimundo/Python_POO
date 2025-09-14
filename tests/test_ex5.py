from ex5 import *
import pytest


def test_positivo():
    celsius = 10
    obj1 = Conversor().celsius_para_fahrenheit(celsius)
    assert obj1 == 50

    fahrenheit = 10
    obj2 = Conversor().fahrenheit_para_celsius(fahrenheit)
    assert obj2 == -12.222222222222221

def test_caracter():
    obj1 = Conversor()
    with pytest.raises(TypeError):
        obj1.celsius_para_fahrenheit('a')

    obj2 = Conversor()
    with pytest.raises(TypeError):
        obj2.fahrenheit_para_celsius('@')
