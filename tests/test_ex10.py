import pytest
from ex10 import Mensagem, Pergunta, Condicao

# ------------------- Teste direto -------------------
def test_fluxo_com_resposta_alice():
    fim = Mensagem("Fim")
    msg_ola = Mensagem("Olá Alice", fim)
    msg_outro = Mensagem("Outro nome", fim)

    condicao = Condicao("nome", "Alice", msg_ola, msg_outro)
    inicio = Pergunta("Qual o seu nome?", "nome", condicao, simulada="Alice")

    contexto = {}
    inicio.executar(contexto)

    assert contexto["nome"] == "Alice"
    assert "Olá Alice" in contexto["log"][-2]


def test_fluxo_com_resposta_outro():
    fim = Mensagem("Fim")
    msg_ola = Mensagem("Olá Alice", fim)
    msg_outro = Mensagem("Outro nome", fim)

    condicao = Condicao("nome", "Alice", msg_ola, msg_outro)
    inicio = Pergunta("Qual o seu nome?", "nome", condicao, simulada="Bob")

    contexto = {}
    inicio.executar(contexto)

    assert contexto["nome"] == "Bob"
    assert "Outro nome" in contexto["log"][-2]


# ------------------- Teste parametrizado -------------------
@pytest.mark.parametrize("resposta, esperado", [
    ("Alice", "Olá Alice"),
    ("Bob", "Outro nome"),
    ("Maria", "Outro nome"),
])
def test_fluxo_parametrizado(resposta, esperado):
    fim = Mensagem("Fim")
    msg_ola = Mensagem("Olá Alice", fim)
    msg_outro = Mensagem("Outro nome", fim)

    condicao = Condicao("nome", "Alice", msg_ola, msg_outro)
    inicio = Pergunta("Qual o seu nome?", "nome", condicao, simulada=resposta)

    contexto = {}
    inicio.executar(contexto)

    assert contexto["nome"] == resposta
    assert esperado in contexto["log"][-2]
