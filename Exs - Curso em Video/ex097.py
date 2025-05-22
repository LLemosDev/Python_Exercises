# Um print especial

def escreva(msg):
    tamanho = len(msg)
    print(f"{"-" * (tamanho + 5)}")
    print("{0:^{1}}".format(msg, tamanho + 5))
    print(f"{"-" * (tamanho + 5)}")


escreva("Olá, Mundo!")
escreva("Frase testanto frases ")
escreva("Python está sendo minha primeira linguagem de programação")