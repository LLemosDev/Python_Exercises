# Função para sortear e somar

from random import randint

def sortear(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print("Sorteando 5 valores para a lista obtemos:", end=" ")
    print(*lista)

def somaPar(lista):
    soma = 0
    for e in lista:
        if e % 2 == 0:
            soma += e

    print(f"A soma dos valores pares de {lista} é {soma}")

numeros = []
sortear(numeros)
somaPar(numeros)
