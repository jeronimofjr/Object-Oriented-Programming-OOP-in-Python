from junkfood import *


def controller():
    maquina = Machine(0, 0)
    while True:
        string = input('$').split()
        if string[0] == 'init':
            maquina = Machine(int(string[1]), int(string[2]))
        elif string[0] == 'show':
            print(maquina.toString())
        elif string[0] == 'set':
            if maquina.gerenciarCompraEAlocacao(int(string[1])):
                print('Fail: indice não existe')
            else:
                print(maquina.setC(int(string[1]), string[2], int(string[3]), float(string[4])))
        elif string[0] == 'limpar':
            maquina.limpar(int(string[1]))
        elif string[0] == 'din':
            maquina.dinheiroVai(float(string[1]))
        elif string[0] == 'comprar':
            if maquina.gerenciarCompraEAlocacao(int(string[1])):
                print('Fail: indice não existe')
            else:
                print(maquina.comprar(int(string[1])))
        elif string[0] == 'troco':
            print(maquina.pedirTroco())
        elif string[0] == 'end':
            break
        else:
            print('Comando inválido')

controller()