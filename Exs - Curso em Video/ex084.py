# Lista composta e analise de dados

temporaria = []
pessoas = []
maior = menor = 0

while True:
    nome = input('Digite o nome: ')
    temporaria.append(nome)
    peso = float(input('Digite o peso: '))
    temporaria.append(peso)

    if len(pessoas) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]

    pessoas.append(temporaria)
    temporaria = []

    resposta = input('Deseja continuar [S/N]: ').strip()

    if resposta in "Nn":
        break

print(f"Foram cadastradas {len(pessoas)} pessoas\n"
      f"O maior peso foi {maior}Kg de ", end="")

for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}, ", end=" ")

print(f"O menor peso foi {menor}Kg de ", end="")

for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}, ", end="")