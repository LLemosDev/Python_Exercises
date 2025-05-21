# Maior e menor valor em Tuplas

from random import randint

numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print(f"Os números orteados foram: {numeros}\n"
      f"O maior valor sorteado foi {sorted(numeros)[-1]}\n"
      f"E o menor foi {sorted(numeros)[0]}")