# Crie uma classe chamada Produto com atributos: nome, preço e quantidade
# Metodo 1: Calcular valor total -> Preço * quantidade
# Metodo 2: Atualizar Quantidade -> atualiza da quantidade de produtos
# Desafio : crie objetos do tipo produto, atualize a qnt de cada um deles

class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def caclularvaltot(self):
        return "O valor total é: ", self.preco * self.quantidade

    def atualiza_quantidade(self):
        self.quantidade = int(input('Digite a nova quantidade para o produto: '))

#Criando lista com vários objetos
produtos = [Produto("Caneta", 5, 10),
            Produto("Iphone 8", 4000, 2),
            Produto("Mochila", 80, 5)]


for produto in produtos:
    produto.atualiza_quantidade()
    print(f"Novo valor total: {produto.caclularvaltot()}")