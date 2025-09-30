# 9. Marketplace (feito com ia para estudo)
# Implemente as classes Produto, Estoque, Pedido, ItemPedido e Pagamento. Regras: não vender sem estoque, cupom válido, cálculo de frete.

# ----------------- Classe Produto -----------------
class Produto:
    def __init__(self, cod, nome, qtde, preco):
        self.cod = cod
        self.nome = nome
        self.qtde = qtde
        self.preco = preco

    def get_quantidade(self):
        return self.qtde

    def diminuir_estoque(self, quantidade):
        if quantidade > self.qtde:
            raise ValueError(f"Estoque insuficiente para {self.nome}!")
        self.qtde -= quantidade

    def aumentar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida para reposição.")
        self.qtde += quantidade

# ----------------- Classe Estoque -----------------
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, cod):
        for p in self.produtos:
            if p.cod == cod:
                return p
        raise ValueError("Produto não encontrado no estoque.")

    def mostrar_estoque(self):
        print("----- Estoque -----")
        for p in self.produtos:
            print(f"{p.nome} (Código: {p.cod}) -> {p.get_quantidade()} unidades")
        print("------------------\n")

# ----------------- Classe ItemPedido -----------------
class ItemPedido:
    def __init__(self, produto, quantidade):
        if quantidade > produto.get_quantidade():
            raise ValueError(f"Estoque insuficiente para {produto.nome}!")

        self.produto = produto
        self.quantidade = quantidade
        # Baixa no estoque
        produto.diminuir_estoque(quantidade)
        # Subtotal + frete (1% do valor do item)
        self.subtotal = (produto.preco * quantidade) * 1.01

    def mostrar_item(self):
        print(f"{self.produto.nome} | Quantidade: {self.quantidade} | Subtotal: R${self.subtotal:.2f}")

# ----------------- Classe Pedido -----------------
class Pedido:
    def __init__(self):
        self.itens = []
        self.total = 0.0
        self.cupom_desconto = 0.0  # percentual, ex: 0.1 = 10%

    def adicionar_item(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)
        self.total += item.subtotal

    def aplicar_cupom(self, percentual):
        if percentual < 0 or percentual > 1:
            raise ValueError("Cupom inválido!")
        self.cupom_desconto = percentual
        self.total *= (1 - percentual)

    def mostrar_pedido(self):
        print("----- Pedido -----")
        for item in self.itens:
            item.mostrar_item()
        print(f"Total com desconto/frete: R${self.total:.2f}")
        print("------------------\n")

# ----------------- Classe Pagamento -----------------
class Pagamento:
    def __init__(self, metodo):
        self.metodo = metodo

    def pagar(self, pedido):
        # Aqui você poderia validar saldo/cartão etc
        return f"Pagamento de R${pedido.total:.2f} realizado com sucesso via {self.metodo}!"


if __name__ == '__main__':
    # Criando produtos
    p1 = Produto(101, "Notebook", 10, 3000)
    p2 = Produto(102, "Mouse", 50, 150)

    # Criando estoque
    estoque = Estoque()
    estoque.adicionar_produto(p1)
    estoque.adicionar_produto(p2)
    estoque.mostrar_estoque()

    # Criando pedido
    pedido = Pedido()
    pedido.adicionar_item(p1, 2)
    pedido.adicionar_item(p2, 5)
    pedido.aplicar_cupom(0.1)  # 10% de desconto
    pedido.mostrar_pedido()

    # Pagamento
    pagamento = Pagamento("Cartão de Crédito")
    print(pagamento.pagar(pedido))

    # Estoque atualizado
    estoque.mostrar_estoque()
