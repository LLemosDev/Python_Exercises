# Valores únicos na lista

numeros = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
    else:
        print("Não vou adicionar. Valor duplicado")

    resposta = input('Deseja Continuar [S/N]? ').strip()

    if resposta in "Nn":
        break

numeros.sort()
print(f"Você digitou os valores {numeros}")