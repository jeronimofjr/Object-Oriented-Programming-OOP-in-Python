

from agiota import *

def controller():
    agiota = Agiota()
    while 1:
        line = input('$').split()
        if line[0] == 'init':
            agiota = Agiota(float(line[1]))
        elif line[0] == 'saldo':
            print(agiota.getSaldo())
        elif line[0] == 'add':
            print(agiota.addCli(line[1], ' '.join(line[2:])))
        elif line[0] == 'emp':
            print(agiota.emprestar(line[1], float(line[2])))
        elif line[0] == 'show':
            print(agiota)
        elif line[0] == 'clientes':
            print(agiota.getClientes())
        elif line[0] == 'res':
            print(agiota.resumo())
        elif line[0] == 'his':
            print(agiota.historicoClientes())
        elif line[0] == 'matar':
            agiota.matar(line[1])
        elif line[0] == 'filtrar':
            print(agiota.filtrar(line[1]))
        elif line[0] == 'rec':
            print(agiota.receber(line[1], float(line[2])))
        elif line[0] == 'end':
            break
        else:
            print('comando inválido')

controller()
