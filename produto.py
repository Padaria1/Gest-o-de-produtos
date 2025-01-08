
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

    def mostrar_detalhes(self):
        return f"Produto: {self.__nome}, Preço: R${self.__preco}"

    def serializar(self):
        return {"nome": self.__nome, "preco": self.__preco}
