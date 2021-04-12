from cinema import *
#from cliente import *

def controller():
    cine = Cinema(0)
    while True:
        string = input('$').split()
        if string[0] == 'init':
            cine = Cinema(int(string[1]))
        elif string[0] == 'show':
            print(cine)
        elif string[0] == 'res':
            cine.reservar(string[1], string[2], int(string[3]))
        elif string[0] == 'out':
            cine.cancelar(string[1])
        elif string[0] == 'end':
            break
        else:
            continue

controller()