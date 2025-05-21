# Emprestimo Bancario

casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o seu salário: '))
anos = int(input('Em quantos anos vai pagar: '))

prestacao = casa/(anos * 12)

if prestacao <= ((salario * 30)/100):
    print(f"\033[32mEMPRESTIMO APROVADO\033[m\nA prestação mensal é de R${round(prestacao, 2)}")
else:
    print(f"\033[31mEMPRESTIMO NEGADO")