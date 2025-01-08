
import os
from produto_eletronico import ProdutoEletronico
from produto_alimenticio import ProdutoAlimenticio
from serializacao import salvar_txt, salvar_json

estoque = []

def menu():
    while True:
        
        print("\nMenu:")
        print("1. Adicionar Produto Eletrônico")
        print("2. Adicionar Produto Alimentício")
        print("3. Listar Produtos")
        print("4. Remover Produto")
        print("5. Salvar Produtos em Arquivo")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Produto Eletrônico: ")
            preco = float(input("Preço: "))
            garantia = int(input("Garantia (em anos): "))
            produto = ProdutoEletronico(nome, preco, garantia)
            estoque.append(produto)
            print("Produto Eletrônico adicionado com sucesso!")
        elif opcao == "2":
            nome = input("Nome do Produto Alimentício: ")
            preco = float(input("Preço: "))
            validade = input("Data de Validade (AAAA-MM-DD): ")
            produto = ProdutoAlimenticio(nome, preco, validade)
            estoque.append(produto)
            print("Produto Alimentício adicionado com sucesso!")
        elif opcao == "3":
            for i, produto in enumerate(estoque, 1):
                print(f"{i}. {produto.mostrar_detalhes()}")
                if isinstance(produto, ProdutoAlimenticio) and not produto.verificar_validade():
                    print("   ** Este produto está fora da validade! **")
        elif opcao == "4":
            for i, produto in enumerate(estoque, 1):
                print(f"{i}. {produto.mostrar_detalhes()}")
            index = int(input("Escolha o número do produto a ser removido: ")) - 1
            if 0 <= index < len(estoque):
                estoque.pop(index)
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado!")
        elif opcao == "5":
            salvar_txt(estoque, "estoque.txt")
            salvar_json(estoque, "estoque.json")
            print("Produtos salvos com sucesso!")
        elif opcao == "6":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
