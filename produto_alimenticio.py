
from produto import Produto
from datetime import datetime

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco, validade):
        super().__init__(nome, preco)
        self.__validade = validade

    @property
    def validade(self):
        return self.__validade

    def mostrar_detalhes(self):
        return f"Produto Alimentício: {self.nome}, Preço: R${self.preco}, Validade: {self.__validade}"

    def verificar_validade(self):
        data_atual = datetime.now()
        validade = datetime.strptime(self.__validade, "%Y-%m-%d")
        return validade >= data_atual

    def serializar(self):
        base = super().serializar()
        base["validade"] = self.__validade
        return base
