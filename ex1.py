# Implemente a classe Conta com atributos numero, titular e saldo (inicial em 0). Métodos: depositar, sacar, extrato. O saque não pode deixar o saldo negativo.

class Conta:
    def __init__(self, numero, titular, saldo=0): 
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        if valor <= 0: 
            raise ValueError('Não é possível depositar sem um valor inteiro!!')
        self.saldo += valor 
        print(f'O valor de R${valor} foi depositado.\nSeu saldo atual é de: R${self.saldo}')

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para retirada!!!")
        self.saldo -= valor
        print(f'O valor de R${valor} foi retirado.\nSeu saldo atual é de: R${self.saldo}')

    def extrato(self):
        print(f'Seu saldo atual é de: R${self.saldo}')

class ContaPoupanca(Conta):

    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.depositar(juros)
        print(f"Juros de R${juros} aplicados. Saldo atual: R${self.saldo}")


class ContaCorrente(Conta):

    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)


if __name__ == "__main__":
    conta_poupanca = ContaPoupanca("Carlos", 1000, 0.02)
    conta_corrente = ContaCorrente("Ana", 500)

    conta_poupanca.extrato()
    conta_poupanca.aplicar_juros()
    conta_poupanca.sacar(200)
    conta_poupanca.extrato()

    conta_corrente.extrato()
    conta_corrente.depositar(300)
    conta_corrente.sacar(100)
    conta_corrente.extrato()    