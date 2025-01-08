
from produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, garantia):
        super().__init__(nome, preco)
        self.__garantia = garantia

    @property
    def garantia(self):
        return self.__garantia

    def mostrar_detalhes(self):
        return f"Produto Eletrônico: {self.nome}, Preço: R${self.preco}, Garantia: {self.__garantia} anos"

    def serializar(self):
        base = super().serializar()
        base["garantia"] = self.__garantia
        return base
