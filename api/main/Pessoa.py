class Pessoa:

    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def _dados_criptografados(self) -> str:
        # Faz o comportamento de criptografia
        return "criptografia real"

    def get_dados_criptografados_maiusculos(self):
        # Faz o comportamento de criptografia
        return self._dados_criptografados().upper()
