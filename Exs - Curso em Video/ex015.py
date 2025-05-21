# Aluguel de Carro
# O carro custa R$60 por dia + R$0.15 por km rodado

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
p = round(60 * d + km * 0.15, 2)
print(f'O preço total a pagar é de R${p}')
