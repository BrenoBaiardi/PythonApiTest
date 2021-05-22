import pytest


@pytest.fixture()
def csv_cores():
    return "cores.csv"


@pytest.fixture()
def popular_csv_cores(csv_cores):
    # setUp
    cores_file = open(csv_cores, mode='w')
    cores_file.writelines("Azul,1")
    cores_file.close()
    yield cores_file.name
    # tearDown
    open(csv_cores, mode='w').close()


def test_ler_cores(popular_csv_cores):
    arquivo_lido = open(popular_csv_cores)
    assert (arquivo_lido.read() == "Azul,1")


def test_arquivo_esta_vazio(csv_cores):
    arquivo_lido = open(csv_cores)
    assert (arquivo_lido.read() == "")


# tmpdir cria uma pasta temporaria pra cada um dos testes
# e faz o teardown automaticamente
def test_criar_um_unico_arquivo(tmpdir):
    tmpdir.mkdir("pasta").join("arquivo.txt")
    print(tmpdir.listdir())
    assert len(tmpdir.listdir()) == 1


# o teste abaixo não é influenciado por arquivo residual na tmpdir
def test_criar_cinco_arquivos(tmpdir):
    for i in range(5):
        open(tmpdir + "/arquivo-{}.txt".format(i), mode="w")
    print(tmpdir.listdir())
    assert len(tmpdir.listdir()) == 5
