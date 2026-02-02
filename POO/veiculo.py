# Exercício: Crie objetos de Carro e Moto e chame o método exibir_detalhes() em cada um.
# Classes Veiculo (superclasse) e Carro, Moto (subclasses)

class Veiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_porta):
        super().__init__(marca, modelo)
        self.num_porta = num_porta

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Num portas: {self.num_porta}')


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Cilindradas: {self.cilindradas}')
    

meu_carro = Carro("Chevrolet", "Caravan", 4)
minha_moto = Moto("Suziki", "GSx-8R", 4)

meu_carro.exibir_detalhes()
minha_moto.exibir_detalhes()