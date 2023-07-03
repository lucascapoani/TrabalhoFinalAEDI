# As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes (marca e modelo).
from Veiculo import Veiculo

# A classe drone é composta dos atributos marca, modelo e quantidade de hélices.
class Drone(Veiculo):
    def __init__(self, marca, modelo, qtdHelices):
        super().__init__(marca, modelo)
        # O atributo quantidade de hélices é fortemente privado.
        self.__qtdHelices = qtdHelices
        self.prox = None

    # Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.
    def imprimir_informacoes(self) -> None:
        super().imprimir_informacoes()
        print(f'Quantidade de Hélices: {self.getHelices()}')

    def getHelices(self):
        return self.__qtdHelices
