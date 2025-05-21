# Criar uma classe que simule um carrinho de compras de um e-commerce, ele permite:
#Iserir e retirar produtos do carrinho de compras e fica em loop

class Produto():
    def __init__(self, nome, preco, quantidade = None):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def detalhes(self):
        print(f"Produto: {self.nome}\n"
              f"Quantidade: {self.quantidade}\n"
              f"Preço: R${self.preco}")

    def calcularvaltot(self):
        return self.preco * self.quantidade

class Carrinho():
    def __init__(self):
        self.carrinho = []

    def mostrar_carrinho(self):
        if len(self.carrinho) > 0:
            print("SEU CARRINHO")
            print('-' * 15)
            for indice, produto in enumerate(self.carrinho):
                print(f"PRODUTO {indice + 1}")
                produto.detalhes()
                print("-" * 20)
        else:
            print("CARRINHO VAZIO")
            return 0

    def inserir_produto(self, produto):
        if isinstance(produto, Produto):
            self.carrinho.append(produto)

    def retirar_produto(self, produto_nome):
        for produto in self.carrinho:
            if produto.nome.lower() == produto_nome.lower():
                self.carrinho.remove(produto)
                print(f"Produto {produto.nome} removido do carrinho")
                return

    def valortotal(self):
        self.valor_carrinho = 0
        for e in self.carrinho:
            self.valor_carrinho += e.calcularvaltot()
        return self.valor_carrinho


lista_produtos = [Produto("Caneta", 2.5), Produto("Lápis", 1.0),
                  Produto("Borracha", 3.0), Produto("Apontador", 2.5),
                  Produto("Caderno", 15.90), Produto("Estojo", 12.50),
                  Produto("Régua", 4.75), Produto("Marca-texto", 6.20),
                  Produto("Corretivo", 5.80), Produto("Grampeador", 22.90)]

carrinho = Carrinho()

print("       LOJA DO JORJÃO")
print("-" * 30)
for i, p in enumerate(lista_produtos):
    print(f"{i + 1} --> {p.nome}  -- R${p.preco:}")
print('-' * 20)

while True:
    print()
    print("1 -- Adicionar item ao carrinho\n"
          "2 -- Remover Item do carrinho\n"
          "3 -- Mostra Carrinho\n"
          "4 -- Mostra Valor total do carrinho\n"
          "5 -- Sair do Programa\n")

    resposta = int(input('O que deseja fazer: '))

    if resposta == 5:
        print("PROGRAMA ENCERRADO")
        break

    elif resposta == 1:
        print()
        for i, p in enumerate(lista_produtos):
            print(f"{i + 1} --> {p.nome}  -- R${p.preco:}")
        print('-' * 20)
        item = int(input("Digite o item que deseja adicionar ao carrinho: "))
        qtd = int(input('Digite a quantidade que deseja adicionar: '))
        lista_produtos[item - 1].quantidade = qtd
        carrinho.inserir_produto(lista_produtos[item - 1])
        print("Item adicionado ao carrinho!")
        print()
    elif resposta == 2:
        retorno = carrinho.mostrar_carrinho()
        if retorno == 0:
            print("Seu carrinho está vazio, não há nada para remover.")
        else:
            nome = input("Digite o nome do produto que deseja remover: ")
            carrinho.retirar_produto(nome)

    elif resposta == 3:
        carrinho.mostrar_carrinho()

    elif resposta == 4:
        print(f"Valor total do carrinho: R${carrinho.valortotal()}")

    else:
        print("Digite um número válido")












