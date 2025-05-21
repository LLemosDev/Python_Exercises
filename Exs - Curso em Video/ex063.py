# Fibonnaci

termos = int(input('Quantos termos você deseja mostrar? '))
a = 0
b = 1

for t in range(0, termos - 2):
    c = a + b
    if t == 0:
        print(a, end=" -> ")
        print(b, end=" -> ")
    print(c, end=" -> ")
    a = b
    b = c
print("Acabou")
