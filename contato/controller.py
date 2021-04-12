from contato import *
from fone import *

def controller():
    usuario = Contato()
    while True:
        string = input('$').split()
        if string[0] == 'show':
            print(usuario)
        elif string[0] == 'init':
            usuario = Contato(string[1])
        elif string[0] == 'add':
            print(usuario.addFone(Fone(string[1], string[2])))
        elif string[0] == 'rm':
            usuario.rmFone(int(string[1]))
        elif string[0] == 'update':
            usuario = Contato(string[1])
            for i in string[2:]:
                fone = i.split(':')
                usuario.addFone(Fone(fone[0], fone[1]))
        elif string[0] == 'end':
            break
        else:
            print('Comando inválido')