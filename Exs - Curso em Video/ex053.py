#Detector de Palíndromo

frase = input('Digite sua frase: ').strip().upper()
palavras = frase.split()    #Divide a frase em uma lista de strings
junto = ''.join(palavras)   #Junta a lista de palavras em uma única sem espaços
inverso = ''
print(palavras)
for letra in range(len(junto) -1 , -1,  -1):  # Pega o ultimo indice da lista e vai diminuindo em 1 té 0
    inverso += junto[letra]

if inverso == junto:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo ")


