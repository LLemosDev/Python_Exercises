#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = str(input('Qual seu nome completo: ')).strip()
x = n.upper().split()
print('SILVA' in x)

