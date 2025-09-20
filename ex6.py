# 6.Folha de Pagamento
# Crie a classe Funcionario e subclasses CLT(salario) e PJ(horas, valor_hora), cada uma com método pagar().
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    @abstractmethod
    def pagar(self):
        pass

class CLT(Funcionario):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome, cargo)
        if salario <= 0:
            raise ValueError('O valor não pode ser negativo')
        self.salario = salario

    def pagar(self):
        ir = 0.1
        inss = 0.2
        desconto = (ir * self.salario) + (inss * self.salario)
        self.salario = self.salario - desconto
        print(f'-----------\n{self.nome}, seu salário de {self.cargo} é: R${self.salario}\nCom descontos de: R${desconto}\n----------')
        return self.salario

class PJ(Funcionario):
    def __init__(self, nome: str, cargo, horas, valor_hora):
        super().__init__(nome, cargo)
        if horas <= 0:
            raise ValueError('O valor não pode ser negativo')
        self.horas = horas
        if valor_hora <= 0:
            raise ValueError('O valor não pode ser negativo')
        self.valor_hora = valor_hora

    def pagar(self):
        receber = self.horas * self.valor_hora
        print(f'----------\n{self.nome}, o valor total a receber como {self.cargo} é de: R${receber}\nTotal de horas trabalhadas: {self.horas}\n----------')
        return receber

if __name__ == '__main__':
    clt = CLT('Camila', 'Analista de Sistemas', 8000)
    clt.pagar()

    pj = PJ('Fabricio', 'Supervisor de TI', 210, 40)
    pj.pagar()

    

    