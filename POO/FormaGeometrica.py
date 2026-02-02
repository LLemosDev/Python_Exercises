# Exercício: Crie uma lista de objetos de Retangulo e Triangulo. Itere pela lista e chame
# os métodos calcular_area() e calcular_perimetro() para cada forma,
# demonstrando o polimorfismo

# FormaGeometrica e classes Retangulo, Triangulo:
from abc import  ABC, abstractmethod

class FormaGeometrica():
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura, nome):
        self.base = base
        self.altura = altura
        self.nome = nome

    def calcular_area(self):
        return round(self.base * self.altura, 2)
    
    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3, nome):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.nome = nome

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_area(self):
        p = self.calcular_perimetro() / 2
        area = (p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3)) ** 0.5
        return round(area, 2)

objetos = [Triangulo(4, 5, 6, "Triângulo"), Retangulo(3, 5, "Retângulo"),
            Triangulo(3, 4, 5, "Triângulo"), Retangulo(7, 5, "Retângulo")]

for o in objetos:
    print(f"{o.nome}, Perimetro: {o.calcular_perimetro()}, Área {o.calcular_area()}")
        
    

    
        