# Validação de dado

sexo = input("Digite seu sexo [M/F]: ").strip().upper()

while sexo != "M" and sexo != "F":
    sexo = input("Dado inválido, informe seu sexo: ").strip().upper()

print("Sexo %s registrado com suceso" % sexo)
    