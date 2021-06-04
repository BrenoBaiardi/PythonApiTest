import os


class CriarArquivo:

    def __init__(self, path):
        self._path = path

    def get_path(self):
        return self._path

    def cria_arquivo(self):
        open(self._path, mode="w")

    def apaga_arquivo(self):
        os.remove(self._path)
