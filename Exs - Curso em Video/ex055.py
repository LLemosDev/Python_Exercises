# Maior e Menor peso

lista = []

for i in range(1, 6):
    peso = float(input(f"Qual o peso da {i} pessoa? "))
    lista.append(peso)

lista.sort()
print(f"O maior peso lido foi {lista[-1]}Kg e o menor {lista[0]}Kg")
