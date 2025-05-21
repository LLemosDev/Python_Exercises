# Extraindo dados de uma lista

numeros = []
resposta = "S"

while resposta in "Ss":
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    resposta = input("Deseja continuar [S/N]").strip()

# Ordenando a lista em ordem decrescente
numeros.sort(reverse = True)
print(f"Foram digitados {len(numeros)} números\n"
      f"A lista de números em ordem decrescente: {numeros}\n")

if 5 in numeros:
    print("O número 5 está na lista e foi digitado")
else:
    print("O número 5 não está na lista e não foi digitado")