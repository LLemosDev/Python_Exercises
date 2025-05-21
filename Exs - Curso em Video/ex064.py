# Tratando vários valores

soma = 0
cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f"Você digitou {cont} números e a soma deles é {soma}")
