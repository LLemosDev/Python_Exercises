# Analise de dados em tupla


nums = (int(input('Digite um número: ')), int(input('Digite um número: ')),
        int(input('Digite um número: ')),int(input('Digite um número: ')))

print("Você digitou os valores:", nums)
print(f"O número 9 apareceu {nums.count(9)} vezes")
if 3 in nums:
      print(f"O número 3 foi digitado pela primeira vez na {nums.index(3) + 1} posição")
else:
      print("O número 3 não foi digitado")
print("Os valores pares digitados foram:", end=" ")

for num in nums:
      if num % 2 == 0:
            print(num, end=" ,")

