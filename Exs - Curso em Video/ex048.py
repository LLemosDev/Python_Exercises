# Soma ímpares múltiplos de três
soma = 0
cont = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        soma += x
        cont += 1

print(f"A soma dos {cont} valores é igual a {soma}")