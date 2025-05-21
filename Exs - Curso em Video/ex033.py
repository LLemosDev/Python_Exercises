# Menor e Maior

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

l = [a, b, c]
l.sort()

print(f"O Maior número é {l[2]}\nO Menor número é {l[0]}")