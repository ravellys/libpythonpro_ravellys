from time import sleep


class Sessao:
    cont = 0
    list = []

    def salvar(self, usuario):
        Sessao.cont += 1
        usuario.id = Sessao.cont
        Sessao.list.append(usuario)

    def listar(self):
        return self.list

    def roll_back(self):
        self.list.clear()

    def fechar(self):
        pass


class Conexao:
    def __init__(self):
        sleep(1)

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
