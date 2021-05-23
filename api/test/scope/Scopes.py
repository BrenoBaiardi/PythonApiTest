import pytest


def test_ler_cores(popular_csv_cores):
    arquivo_lido = open(popular_csv_cores)
    assert (arquivo_lido.read() == "Azul,1")


def test_arquivo_esta_vazio(csv_cores):
    arquivo_lido = open(csv_cores)
    assert (arquivo_lido.read() == "")


# tmpdir cria uma pasta temporaria pra cada um dos testes
# e faz o teardown automaticamente
def test_criar_um_unico_arquivo(tmpdir):
    tmpdir.join("arquivo").write("texto")
    assert len(tmpdir.listdir()) == 1


# o teste abaixo não é influenciado por arquivo residual na tmpdir
def test_criar_cinco_arquivos(tmpdir):
    for i in range(5):
        open(tmpdir + "/arquivo-{}.txt".format(i), mode="w")
    assert len(tmpdir.listdir()) == 5


def test_ler_arquivo_alterado_usando_tmpdir(criar_arquivo_customizado_com_tmpdir):
    arquivo = criar_arquivo_customizado_com_tmpdir
    print("\n->Path sendo utilizado: {}".format(arquivo.dirname))
    print("\n->{0}".format(arquivo.read()))
    arquivo.write("texto alterado")
    print("\n->{0}".format(arquivo.read()))


def test_ler_arquivo_original_usando_tmpdir(criar_arquivo_customizado_com_tmpdir):
    arquivo = criar_arquivo_customizado_com_tmpdir
    print("\n->Path sendo utilizado: {}".format(arquivo.dirname))
    print("\n->{0}".format(arquivo.read()))
