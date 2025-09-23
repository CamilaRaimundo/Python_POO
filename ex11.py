# 11.Sistema de Reserva de Salas
# Implemente Sala(capacidade) e Reserva(sala, inicio, fim). A Agenda deve impedir sobreposição de horários.

class Sala():
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Reserva():
    def __init__(self, sala, inicio, fim):
        self.sala = sala 
        self.inicio = inicio
        self.fim = fim 

    def agendar():
        pass