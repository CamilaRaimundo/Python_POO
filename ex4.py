# 4.Agenda de Contatos
# Crie a classe Contato(nome, email). Dois contatos devem ser considerados iguais se tiverem o mesmo e-mail. 

class Contato():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email 


class Agenda(): 
    
    def __init__(self):
        self.contatos = {}      

    def adicionar(self, contato): 
        if contato.email in self.contatos:
            raise ValueError('O e-mail já existe!!')
        else:
            self.contatos[contato.email] = contato.nome

    def listar(self):
        if not self.contatos:
            print("\Agenda Vazia\n")
        else:
            print(self.contatos)

if __name__ == '__main__':
    obj = Contato(nome="Camila", email="aaaaaaa")
    obj2 = Contato(nome="Camila2", email="aaaaaaa")

    agenda = Agenda()
    
    agenda.adicionar(obj)

    agenda.listar()