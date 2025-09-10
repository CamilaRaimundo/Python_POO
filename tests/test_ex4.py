import pytest
from ex4 import Contato, Agenda


@pytest.fixture
def contato1():
    return Contato("Camila", "camila@email.com")

@pytest.fixture
def contato2():
    return Contato("Fabrício", "fabricio@email.com")

@pytest.fixture
def contato_dup():
    return Contato("Camila 2", "camila@email.com")

@pytest.fixture
def agenda():
    return Agenda()


def test_agenda_vazia(agenda):
    assert agenda.contatos == {}  # deve iniciar vazia


def test_adicionar_contato(agenda, contato1):
    agenda.adicionar(contato1)
    assert contato1.email in agenda.contatos
    assert agenda.contatos[contato1.email] == contato1.nome


def test_adicionar_dois_contatos(agenda, contato1, contato2):
    agenda.adicionar(contato1)
    agenda.adicionar(contato2)
    assert len(agenda.contatos) == 2


def test_nao_permite_email_duplicado(agenda, contato1, contato_dup):
    agenda.adicionar(contato1)
    with pytest.raises(ValueError, match="O e-mail já existe!!"):
        agenda.adicionar(contato_dup)
