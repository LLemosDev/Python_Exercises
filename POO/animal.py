# Exercício: Crie objetos de Cachorro e Gato, chame os métodos emitir_som(), 
# latir() (para cachorro) e miar() (para gato). Demonstre o
# polimorfismo ao chamar emitir_som() em objetos de ambas as classes.

class Animal():
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return 'som genérico do animal'
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"
    
    def latir(self):
        return "Woof Woof!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
    def miar(self):
        return "Meow Meow!"

meu_cachorro = Cachorro("Luma")
meu_gato = Gato("Garfield")

print(meu_cachorro.emitir_som(), meu_cachorro.latir())
print(meu_gato.emitir_som(), meu_gato.miar())