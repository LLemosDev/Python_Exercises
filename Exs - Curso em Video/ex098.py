# Função de Contador
from time import sleep
def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} a {fim} de {passo} em {passo}")
    print("=-" * 18)
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ")
            sleep(0.5)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=" ")
            sleep(0.5)
    print("FIM!")
    print("=-" * 18)

contador(1, 10, 1)
contador(10, 0, 2)

print("Contagem Personalizada")
inicio = int(input("Começar a contar a partir do: "))
fim = int(input("Parar de contar no: "))
passo = int(input("Pulando de quantos em quantos: "))

contador(inicio, fim, passo)