
Sistema de Gestão de Produtos

apresento meu projeto livre de OO em Python para gerenciar produtos em um estoque.

Conceitos de OO Aplicados:
- Herança `ProdutoEletronico` e `ProdutoAlimenticio` herdam da classe base `Produto`.
- Polimorfismo: O método `mostrar_detalhes()` é polimórfico, ou seja, tem comportamentos diferentes dependendo do tipo do produto.
- Encapsulamento: Todos os atributos dos produtos são privados, sendo acessados apenas por métodos públicos (getter).

Funcionalidades:
- Serialização de Objetos: O sistema permite salvar os produtos em arquivos `.txt` e `.json`.
- Verificação de Validade: Produtos alimentícios possuem verificação de validade antes de serem listados.

Exemplo de Execução:

python main.py
