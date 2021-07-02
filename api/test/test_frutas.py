import pytest


class Fruta:
    def __init__(self, nome):
        self.nome = nome

    def __eq__(self, other):
        return self.nome == other.nome


@pytest.fixture
def minha_fruta():
    return Fruta("maçã")


@pytest.fixture
def cesto():
    return []


@pytest.fixture
def cesto_de_frutas(cesto, minha_fruta):
    cesto.append(minha_fruta)
    return cesto


def test_fruta_no_cesto(minha_fruta, cesto_de_frutas):
    assert minha_fruta in cesto_de_frutas


def test_cesto_vazio(cesto):
    assert len(cesto) == 0


def test_fruta_maca(minha_fruta):
    assert minha_fruta.nome == "maçã"
