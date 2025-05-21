# Resolução usando int - inteiro

n = int(input('Digite um número entre 0 e 9999: '))
print(f'Analisando o número {n}')
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000
print(f'Unidade: {u} \n'
      f'Dezena: {d} \n'
      f'Centena: {c} \n'
      f'Milhar: {m}')


