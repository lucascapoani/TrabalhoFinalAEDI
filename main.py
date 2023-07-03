from pilhaDrones import PilhaDrones
from pilhaCarros import PilhaCarros

pilhaCarros = PilhaCarros()
pilhaDrones = PilhaDrones()

# Implemente uma tela com um menu (funcionando) que permita ao usuário:
# -> Adicionar e remover carros da Pilha.
# -> Adicionar e remover drones da Pilha.
# -> Imprimir a Pilha de carros e a Pilha de drones.

while True:
    option = input('''BEM VINDO! ESCOLHA UMA DAS OPÇÕES ABAIXO:
1 - ADICIONAR CARRO
2 - REMOVER CARRO
3 - ADICIONAR DRONE
4 - REMOVER DRONE
5 - IMPRIMIR PILHA DE CARROS
6 - IMPRIMIR PILHA DE DRONES
7 - FINALIZAR O PROGRAMA

ESCOLHA: 
''')

    if option == '1':
        marca = input('MARCA DO CARRO: ')
        modelo = input('MODELO DO CARRO: ')
        portas = input('QUANTIDADE DE PORTAS: ')
        pilhaCarros.addCarro(marca,modelo,portas)
    
    elif option == '2':
        pilhaCarros.remove()
    
    elif option == '3':
        marca = input('MARCA DO DRONE: ')
        modelo = input('MODELO DO DRONE: ')
        helices = input('QUANTIDADE DE HÉLICES: ')
        pilhaDrones.addDrone(marca,modelo,helices)
    
    elif option == '4':
        pilhaDrones.remove()

    elif option == '5':
        pilhaCarros.printCarros()

    elif option == '6':
        pilhaDrones.printDrones()
    
    elif option == '7':
        print('OPERAÇÃO FINALIZADA!')
        break
    print('==--==--==--==--==--==--==--==--==')
