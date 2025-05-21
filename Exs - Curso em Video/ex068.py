# Jogo par ou ímpar

from random import randint

print("Jogo Par ou Ímpar")
print("=-" * 12)
cont = 0
while True:
    computador = randint(1, 10)
    valor = int(input('Digite o valor: '))
    escolha = input('Par ou Ímpar [P/I]: ').strip().upper()
    soma = computador + valor
    if soma % 2 == 0:
        num = "Par"
    else:
        num = "Ímpar"
    if num == "Par" and escolha == "P":
        cont += 1
        print(f"Você jogou {valor} e o computador {computador}. Total de {soma}, o que é par")
        print("Você venceu\nVamos jogar de novo...")

    elif num == "Ímpar" and escolha == "I":
        cont += 1
        print(f"Você jogou {valor} e o computador {computador}. Total de {soma}, o que é Ímpar")
        print("Você venceu\nVamos jogar de novo...")

    else:
        print(f"Você jogou {valor} e o computador {computador}. Total de {soma}, o que é {num}")
        print(f"GAME OVER, você venceu {cont} vezes")
        break
