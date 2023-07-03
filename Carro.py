# As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes (marca e modelo).
from Veiculo import Veiculo

# A classe carro é composta dos atributos marca, modelo e portas.
class Carro(Veiculo):
    def __init__(self, marca, modelo, qtdPortas):
        super().__init__(marca, modelo)
        # O atributo portas é fracamente privado.
        self._qtdPortas = qtdPortas
        self.prox = None

    # Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'Quantidade de Portas: {self._qtdPortas}')

    def getQtdPortas(self):
        return self._qtdPortas
