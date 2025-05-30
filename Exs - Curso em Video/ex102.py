# Função fatorial

def fatorial(num, show=False):
    resultado = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
        resultado *= i
    print(resultado)


fatorial(5, True)
fatorial(5)
fatorial(8, True)
fatorial(0, show=True)