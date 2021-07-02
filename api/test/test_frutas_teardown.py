import pytest


class Fruta:
    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, other):
        return self.nome == other.nome


@pytest.fixture
def minha_fruta() -> Fruta:
    return Fruta("maçã")


@pytest.fixture
def cesto() -> list:
    return []


@pytest.fixture
def cesto_em_arquivo(cesto, minha_fruta):
    cesto.append(minha_fruta)
    with open("cesto.txt", mode="a") as arquivo:
        for fruta in cesto:
            arquivo.write(fruta.nome)
        arquivo.close()


# @pytest.fixture
# def cesto_em_arquivo(cesto, minha_fruta):
#     cesto.append(minha_fruta)
#     with open("cesto.txt", mode="a") as arquivo:
#         for fruta in cesto:
#             arquivo.write(fruta.nome)
#         arquivo.close()
#     yield
#     open("cesto.txt", mode="w")  # recria o arquivo vazio


def test_cesto_em_arquivo(cesto_em_arquivo):
    # arquivo não existe
    cesto_em_arquivo  # chama a função para ser executada
    # arquivo existe
    with open("cesto.txt", mode="r") as arquivo:
        assert arquivo.read() == "maçã"


def test_cesto_em_arquivo_novamente(cesto_em_arquivo):
    # arquivo não existe
    cesto_em_arquivo  # chama a função para ser executada
    # arquivo existe
    with open("cesto.txt", mode="r") as arquivo:
        assert arquivo.read() == "maçã"
