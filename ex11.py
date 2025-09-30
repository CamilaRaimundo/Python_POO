# 11.Sistema de Reserva de Salas (feito com ia para estudo)
# Implemente Sala(capacidade) e Reserva(sala, inicio, fim). A Agenda deve impedir sobreposição de horários.

class Sala:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade

class Reserva:
    def __init__(self, sala: Sala, inicio: int, fim: int):
        if fim <= inicio:
            raise ValueError("O horário de fim deve ser maior que o de início.")

        self.sala = sala
        self.inicio = inicio
        self.fim = fim

    def conflita(self, outra: "Reserva") -> bool:
        return not (self.fim <= outra.inicio or self.inicio >= outra.fim)

class Agenda:
    def __init__(self):
        self.reservas = []

    def agendar(self, reserva: Reserva) -> bool:
        for r in self.reservas:
            if r.sala == reserva.sala and r.conflita(reserva):
                return False
        self.reservas.append(reserva)
        return True
    
if __name__ == "__main__":
    sala1 = Sala(20)
    agenda = Agenda()

    r1 = Reserva(sala1, 14, 16)
    r2 = Reserva(sala1, 15, 17)
    r3 = Reserva(sala1, 16, 18)

    print("Agendando r1 (14-16):", agenda.agendar(r1))  # True
    print("Agendando r2 (15-17):", agenda.agendar(r2))  # False (conflita com r1)
    print("Agendando r3 (16-18):", agenda.agendar(r3))  # True (encaixa depois de r1)

    print("\nReservas confirmadas:")
    for r in agenda.reservas:
        print(f" - Sala({r.sala.capacidade} pessoas): {r.inicio}h às {r.fim}h")
