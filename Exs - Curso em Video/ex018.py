# Calculando seno, cosseno e tangente

import math

A = int(input('Digite o valor do ângulo: '))
r = math.radians(A)
senA = round(math.sin(r), 2 )
cosA = round(math.cos(r), 2)
tgA = round(math.tan(r), 2)
print(f'Ângulo de {A}° tem: \n'
      f'Seno = {senA} \n'
      f'Cosseno = {cosA} \n'
      f'Tangente = {tgA}')



