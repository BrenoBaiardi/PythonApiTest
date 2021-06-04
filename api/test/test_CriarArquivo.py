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


def test_cria_arquivo(get_criar_arquivo_com_cleanup):
    get_criar_arquivo_com_cleanup.cria_arquivo()
    assert len(os.listdir("C:\\Users\\Breno Baiardi\\PycharmProjects\\Rest-Api-Test\\api\\test\\temp")) == 1


# Abaixo com fixture default


@pytest.fixture()
def get_criar_arquivo_em_tmpdir(tmpdir):
    print(tmpdir)
    criar_arquivo = CriarArquivo("{}\\nome_do_arquivo.txt".format(tmpdir))
    return criar_arquivo


def test_cria_arquivo_com_default(get_criar_arquivo_em_tmpdir,tmpdir):
    get_criar_arquivo_em_tmpdir.cria_arquivo()
    assert len(os.listdir(tmpdir)) == 1
