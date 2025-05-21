# Maior, Menor e Média

soma = 0
cont = 0
maior = 0
menor = 0
nums = []

while True:
    num = int(input("Digite um número: "))
    cont += 1
    nums.append(num)
    soma += num
    continua = input('Deseja continuar S/N ? ').strip().upper()
    if continua == "N":
        break

nums.sort()
print(f"Você digitou {cont} números \nA média dos números é {round(soma / cont, 2)}\n"
      f"O maior número digitado foi {nums[-1]} e o menor {nums[0]}")