# Fatorial

num = int(input("Digite o número para calcular seu fatorial: "))
fatorial = 1

for i in range(num, 1, -1):
    fatorial *= i
print(fatorial)

