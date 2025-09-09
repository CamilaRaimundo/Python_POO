# 3. Biblioteca de Mídias
# Crie a classe Midia(titulo, ano) e subclasses Filme(duracao) e Livro(paginas). Inclua uma propriedade idade calculada a partir do ano.

from datetime import date

class Midias():
    def __init__(self, titulo, ano, idade_calculada=0):
        if ano <= 0:
            raise ValueError('O valor não pode ser negativo')
        if ano > date.today().year:
            raise ValueError('Insira um valor válido')
        self.titulo = titulo
        self.ano = ano 
        self.idade_calculada = date.today().year - ano

class Filme(Midias):
    def __init__(self, titulo, ano, duracao, idade_calculada=0):
        super().__init__(titulo, ano, idade_calculada=0)
        if duracao <= 0:
            raise ValueError('O valor não pode ser negativo')
        self.duracao = duracao

class Livro(Midias):
    def __init__(self, titulo, ano, paginas, idade_calculada=0):
        super().__init__(titulo, ano, idade_calculada=0)
        if paginas <= 0:
            raise ValueError('O valor não pode ser negativo')
        self.paginas = paginas


if __name__ == '__main__':
    obj = Livro("Camila", 2005, 650)
    print(f'O livro chama-se: {obj.titulo}')
    print(f'Ele possui {obj.paginas} página')
    print(f'Tem a idade de: {obj.idade_calculada} anos')