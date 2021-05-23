import pytest

from api.main.Pessoa import Pessoa


def test_pessoa_get_nome():
    pessoa = Pessoa("qualquer")
    assert pessoa.get_nome() == "qualquer"


def test_pessoa_get_criptografia(monkeypatch):
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_cripto(*args, **kwargs):
        return "retorno com patch"
    monkeypatch.setattr(Pessoa, "_dados_criptografados", mock_cripto)

    # faz o assert
    pessoa = Pessoa("qualquer")
    assert pessoa.get_dados_criptografados_maiusculos() == "RETORNO COM PATCH"
