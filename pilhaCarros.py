from Carro import Carro

class PilhaCarros:
    def __init__(self):
        self.top = None

    def printCarros(self):
        print('***********************')
        if not self.top:
            return print("Pilha vazia.")
        temp = self.top
        while temp:
            temp.imprimir_informacoes()
            temp = temp.prox
        print('***********************')

    def addCarro(self, marca, modelo, qtdPortas):
        carro = Carro(marca, modelo, qtdPortas)
        if not self.top:
            self.top = carro
        else:
            carro.prox = self.top
            self.top = carro
        print('Carro adicionado com sucesso à pilha')

    def remove(self):
        if not self.top:
            return print("Pilha vazia.")
        if self.top.prox == None:
            self.top = None
        else:
            self.top = self.top.prox
        print('Carro removido da pilha.')
