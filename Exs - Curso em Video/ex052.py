# Numero Primo

# Lógica 1
print("Lógica 1")

soma = 0
num = int(input('Digite um número: '))

for i in range(1, num + 1):
    if num % i == 0:
        soma += i

if soma == num + 1:
    print(f"O Número {num} é primo, pois a soma dos divisores é {num + 1}")
else:
    print(f"O Número {num} não é primo")

# Lógica 2
print('Lógica 2')
li = []

for x in range(1, num + 1):
    if num % x == 0:
        li.append(x)

if li == [1, num]:
    print(f"O Número {num} é primo, pois só é dividido por {li}")
else:
    print(f"O Número {num} não é primo")