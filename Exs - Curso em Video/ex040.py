# Media

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

if m >= 7:
    print(f"\033[32mAPROVADO\033[m sua média final é de {round(m, 2)}")
elif (m >= 5) and (m <= 6.9):
    print(f"\033[33mRECUPERAÇÃO\033[m sua média é de {round(m, 2)}")
else:
    print(f"\033[31mREPROVADO\033[m sua média final é de {round(m, 2)}")