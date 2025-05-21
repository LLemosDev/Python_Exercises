# Unindo dicionário e listas

pessoas = []
media = 0
soma = 0

# Estrutura principal - cadastra a pessoa e adiciona na lista de pessoas
while True:
    pessoa = {'nome': input('Nome: '), 'idade': int(input('Idade: '))}
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()

    while pessoa['sexo'] not in "MF":
        print('Insira apenas M/F: ')
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()

    pessoas.append(pessoa)

    resposta = input('Deseja continuar [S/N]: ').strip().upper()
    while resposta not in "SN":
        print("Insira somente S/N")
        resposta = input('Deseja continuar [S/N]: ').strip().upper()

    if resposta == "N":
        break

print("-=" * 30)
print(f"Ao todo foram cadastradas {len(pessoas)} pessoas ")
# Loop que soma todas as idades
for i in range(len(pessoas)):
    soma += pessoas[i]['idade']

# Calculo da media
media = soma / len(pessoas)
print(f"A média de idade é {round(media, 2)} anos")

mulheres = []

# Loop que verifica as mulheres foram cadastradas
for p in pessoas:
    if p['sexo'] == "F":
        mulheres.append(p['nome'])

print("Mulheres Cadastradas: ", end="")
for m in mulheres:
    print(m, end=" ")

print()

acima_media = []

# Loop que verifica e adiciona pessoas com idade acima da media
for x in pessoas:
    if x['idade'] > media:
        acima_media.append(x['nome'])

print(f"Pessoas que estão acima da média de idade:")
for n in acima_media:
    print(n)
