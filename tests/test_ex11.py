import pytest
from ex11 import Sala, Reserva, Agenda

def test_reserva_valida():
    sala = Sala(10)
    r1 = Reserva(sala, 14, 16)
    r2 = Reserva(sala, 16, 18)  # não conflita
    agenda = Agenda()

    assert agenda.agendar(r1) is True
    assert agenda.agendar(r2) is True
    assert len(agenda.reservas) == 2

def test_reserva_conflitante():
    sala = Sala(20)
    r1 = Reserva(sala, 10, 12)
    r2 = Reserva(sala, 11, 13)  # sobrepõe
    agenda = Agenda()

    assert agenda.agendar(r1) is True
    assert agenda.agendar(r2) is False
    assert len(agenda.reservas) == 1

def test_reservas_salas_diferentes():
    sala1 = Sala(15)
    sala2 = Sala(30)
    r1 = Reserva(sala1, 9, 11)
    r2 = Reserva(sala2, 9, 11)  # mesmo horário, mas outra sala

    agenda = Agenda()
    assert agenda.agendar(r1) is True
    assert agenda.agendar(r2) is True
    assert len(agenda.reservas) == 2

def test_horario_invalido():
    sala = Sala(10)
    with pytest.raises(ValueError):
        Reserva(sala, 14, 13)  # fim antes do início
