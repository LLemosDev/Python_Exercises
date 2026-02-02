# Exercício: Crie objetos da classe Círculo com diferentes raios e imprima suas áreas e perímetros

PI = 3.14

class Circulo():
    # Vamos considerar raio em m
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return round(PI * self.raio ** 2, 2)
    
    def calcula_perimetro(self):
        return round(2 * PI * self.raio, 2)
    

circulos = [Circulo(2), Circulo(3), Circulo(5), Circulo(7)]

for c in circulos:
    print(f"Perímetro: {c.calcula_perimetro()}m | Área: {c.calcular_area()}m²")

