# Contando vogais em tuplas

palavras = ("abobora", "banana", "pepino", "uva", "melancia")
vogais = ("a", "e", "i", "o", "u")

for i in palavras:
    print(f"\nA palavra {i} tem as seguintes vogais: ", end="")
    for letra in i:
        if letra in vogais:
            print(letra, end=" ")