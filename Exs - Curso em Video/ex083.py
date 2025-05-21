# Validação expressões matemáticas
# Usando lógica de pilhas LIFO (Last In First Out)

exprressao = input('Digite a sua expressão: ').strip()
verificador = []

for c in exprressao:
    if c == "(":
        verificador.append(c)
    elif c == ")":
        if len(verificador) > 0:
            verificador.pop()
        else:
            verificador.append(c)
            break


if len(verificador) == 0:
    print("Expressão válida!")
else:
    print("Expressão Inválida!")