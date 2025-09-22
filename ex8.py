# 8. Sistema de Arquivos (mini)
# Crie Arquivo(tamanho) e Pasta que contém arquivos e outras pastas. Ambas devem ter o método tamanho_total().

class Arquivo():
    def __init__(self, tamanho):
        if tamanho <= 0:
            raise ValueError('O valor não pode ser negativo')
        self.tamanho = tamanho

    def tamanho_total(self):
        return self.tamanho

class Pasta:
    def __init__(self):
        self.itens = []  # pode ter Arquivos ou outras Pastas

    def adicionar(self, item):
        self.itens.append(item)

    def tamanho_total(self):
        tam_total = 0
        for item in self.itens:
            tam_total += item.tamanho_total()  # recursividade 
            #como cada item (seja arquivo ou pasta) tem um método tamanho_total(), a pasta só precisa chamar esse método em cada item e somar.
        return tam_total
        

if __name__ == '__main__':
    arquivo1 = Arquivo(10)
    arquivo2 = Arquivo(20)

    pasta = Pasta()
    pasta.adicionar(arquivo1)
    pasta.adicionar(arquivo2)

    subpasta = Pasta()
    subpasta.adicionar(Arquivo(5))
    subpasta.adicionar(Arquivo(15))

    pasta.adicionar(subpasta)

    print(f'O tamanho total é: {pasta.tamanho_total()}')