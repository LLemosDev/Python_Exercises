"""Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra "A", em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez."""

f = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {f.count('A')} vezes \n'
      f'O primeiro A aparece na posição {f.find('A')+1} \n'
      f'O último A aparece na posição {f.rfind('A')+1}')


