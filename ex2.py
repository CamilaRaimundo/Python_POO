class Item: 
    def __init__(self, nome, preco, qtd=1):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo!")
        if qtd <= 0:
            raise ValueError("Quantidade deve ser maior que zero!")
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def subtotal(self):
        return self.preco * self.qtd


class Carrinho:
    def __init__(self):
        self.itens = [] 

    def adicionar(self, item):
        self.itens.append(item)

    def listar_itens(self):
        for item in self.itens:
            yield item.nome, item.qtd, item.preco, item.subtotal()
        
    def total(self):
        return sum(item.subtotal() for item in self.itens)


if __name__ == '__main__':
    livro = Item("Outro dia", 20, 2)
    livro2 = Item("Algum dia", 10, 3)

    carrinho = Carrinho()
    carrinho.adicionar(livro)
    carrinho.adicionar(livro2)

    print("Itens no carrinho:")
    for nome, qtd, preco, subtotal in carrinho.listar_itens():
        print(f"{qtd}x {nome} a R${preco:.2f} cada → Subtotal: R${subtotal:.2f}")
    print(f"Total do carrinho: R${carrinho.total():.2f}")
