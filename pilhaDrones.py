from Drone import Drone

class PilhaDrones:
    def __init__(self):
        self.top = None

    def printDrones(self):
        print('***********************')
        if not self.top:
            return print("Pilha vazia.")
        temp = self.top
        while temp:
            temp.imprimir_informacoes()
            temp = temp.prox
        print('***********************')

    def addDrone(self, marca, modelo, qtdHelices):
        drone = Drone(marca, modelo, qtdHelices)
        if not self.top:
            self.top = drone
        else:
            drone.prox = self.top
            self.top = drone
        print('Drone adicionado com sucesso à pilha!')

    def remove(self):
        if not self.top:
            return print("Pilha vazia.")
        if self.top.prox == None:
            self.top = None
        else:
            self.top = self.top.prox
        print('Drone removido da pilha.')
