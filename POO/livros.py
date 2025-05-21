# Crie uma classe chamada Livro com os seguintes atributos: Titulo, Autor, Numero de paginas
# Metodos: detalhes - imprime todos os atributos do livro

# Desafio
# Crie uma lista dos objetos de objetos de tipo livro e imprima os detalhes de cada um deles

class Livro():
    def __init__(self, nome, autor, numero_paginas):
        self.nome = nome
        self.autor = autor
        self.numero_paginas = numero_paginas

    def detalhes(self):
        print(f"Nome do livro: {self.nome}\n"
              f"Autor: {self.autor}\n"
              f"Número de Páginas: {self.numero_paginas}")


livros = [Livro("Introdução a Programação com Python", "Nilo Ney", 325),
          Livro("Dom Casmurro", "Machado de Assis", 432),
          Livro("O Pequeno Príncipe", "Saint-Exupéry", 387)]

for livro in livros:
    livro.detalhes()
    print()