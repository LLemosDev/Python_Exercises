# Tabuada 3.0

print("TABUADA -- DIGITE 0 PARA PARAR")
num = int(input('Deseja ver a tabuada de qual valor: '))

while num != 0:
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
    num = int(input('Deseja ver a tabuada de qual valor: '))