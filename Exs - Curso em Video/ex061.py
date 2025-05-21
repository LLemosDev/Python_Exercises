# Progressão Artmética 2.0

t1 = int(input("Digite o valor do primeiro termo: "))
razao = int(input("Digite a razão da progressão: "))
cont = 0

while cont < 10:
    print(t1, "->", end=" ")
    t1 += razao
    cont += 1
print("ACABOU")