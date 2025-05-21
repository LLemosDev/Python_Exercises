"""Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

n = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer! \n' 
      f'Seu primeiro nome é {n.split()[0]} \n'
      f'Seu úlimo nome é {n.split()[-1]}')