n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
print(f'Seu nome tem {len(n) - n.count(' ')} letras')
n1 = n.split()
print(f'Seu primeiro nome é {n1[0]} e tem {len(n1[0])} letras')




