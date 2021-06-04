import pytest
import os
from api.main.CriarArquivo import CriarArquivo


@pytest.fixture()
def get_criar_arquivo():
    criar_arquivo = CriarArquivo("temp\\nome_do_arquivo.txt")
    return criar_arquivo


@pytest.fixture()
def get_criar_arquivo_com_cleanup():
    criar_arquivo = CriarArquivo("temp\\nome_do_arquivo.txt")
    yield criar_arquivo
    criar_arquivo.apaga_arquivo()


def test_cria_arquivo(get_criar_arquivo):
    get_criar_arquivo.cria_arquivo()
    assert len(os.listdir("C:\\Users\\Breno Baiardi\\PycharmProjects\\Rest-Api-Test\\api\\test\\temp")) == 1


# Abaixo com fixture default
