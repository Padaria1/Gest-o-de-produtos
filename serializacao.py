
import json

def salvar_txt(produtos, arquivo):
    with open(arquivo, "w") as f:
        for produto in produtos:
            f.write(produto.mostrar_detalhes() + "\n")

def salvar_json(produtos, arquivo):
    with open(arquivo, "w") as f:
        json.dump([produto.serializar() for produto in produtos], f, indent=4)
