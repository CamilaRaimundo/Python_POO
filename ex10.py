# # 10.Motor de Fluxo de Chatbot (feito com ia para estudo)
# Crie a classe "Nó" com método executar(contexto) e subclasses como Mensagem, Pergunta e Condicao. O fluxo deve executar nós encadeados.

class No:
    def __init__(self, proximo=None):
        self.proximo = proximo

    def executar(self, contexto):
        raise NotImplementedError("Cada nó deve implementar o método executar.")

    def avancar(self, contexto):
        if self.proximo:
            self.proximo.executar(contexto)

# ----------------- Mensagem -----------------
class Mensagem(No):
    def __init__(self, texto, proximo=None):
        super().__init__(proximo)
        self.texto = texto

    def executar(self, contexto):
        contexto.setdefault("log", []).append(f"MENSAGEM: {self.texto}")
        self.avancar(contexto)

# ----------------- Pergunta -----------------
class Pergunta(No):
    def __init__(self, texto, chave, proximo=None, simulada=None):
        """
        simulada: resposta simulada para testes (em vez de usar input)
        """
        super().__init__(proximo)
        self.texto = texto
        self.chave = chave
        self.simulada = simulada

    def executar(self, contexto):
        if self.simulada is not None:
            resposta = self.simulada
        else:
            resposta = input(self.texto + " ")

        contexto[self.chave] = resposta
        contexto.setdefault("log", []).append(f"PERGUNTA: {self.texto} -> {resposta}")
        self.avancar(contexto)

# ----------------- Condicao -----------------
class Condicao(No):
    def __init__(self, chave, valor, no_se, no_senao):
        super().__init__()
        self.chave = chave
        self.valor = valor
        self.no_se = no_se
        self.no_senao = no_senao

    def executar(self, contexto):
        condicao_ok = contexto.get(self.chave) == self.valor
        contexto.setdefault("log", []).append(
            f"CONDICAO: {self.chave} == {self.valor}? {condicao_ok}"
        )

        if condicao_ok:
            self.no_se.executar(contexto)
        else:
            self.no_senao.executar(contexto)


if __name__ == "__main__":
    fim = Mensagem("Obrigado por participar!")
    msg_ola = Mensagem("Olá Alice, bem-vinda!", fim)
    msg_outro = Mensagem("Oi, prazer em te conhecer!", fim)

    condicao = Condicao("nome", "Alice", msg_ola, msg_outro)
    inicio = Pergunta("Qual o seu nome?", "nome", condicao, simulada="Alice")

    contexto = {}
    inicio.executar(contexto)
    print("\nLOG DE EXECUÇÃO:", contexto["log"])
