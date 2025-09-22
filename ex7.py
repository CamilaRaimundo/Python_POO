# 7.Formas Geométricas
# Implemente Forma com método area e reescreva para cada forma. Subclasses: Circulo, Retangulo. Escreva função que receba uma lista de formas e calcule a soma das áreas.

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        if raio <= 0:
            raise ValueError('Não pe possível valores negativos!')
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio
    

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError('Não é possível valores negativos!')
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base*2) + (self.altura*2)

if __name__ == '__main__':
    circulo = Circulo(raio=10)
    print(circulo.area())
    print(circulo.perimetro())

    retangulo = Retangulo(base=10, altura=5)
    print(retangulo.area())
    print(retangulo.perimetro())