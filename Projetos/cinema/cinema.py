from cliente import *

class Cinema:

    def __init__(self, lotacao):
        self.cadeiras = [ None for _ in range(0, lotacao)]
        self.lotacao = lotacao
    
    def __str__(self): 
        return '[ ' + '  '.join([' - ' if i is None else i.toString() for i in self.cadeiras ]) + ' ]'
       
    def reservar(self, name, fone, indice):
        if name in self.getIds():
            print ('fail: cliente ja esta no cinema')
            return False
        if self.cadeiras[indice] == None:
            self.cadeiras[indice] = Cliente(name, fone)
            print('sucess: cliente adicionado')
            return True
        else:
            print('fail: cadeira ja está ocupada')
            return False
        
    def cancelar(self, name):
        if name not in self.getIds():
            print('fail: id não existe')
            return False
        else:
            for i in range(0, self.lotacao):
                if  self.cadeiras[i] != None and  self.cadeiras[i].getId() == name:
                    self.cadeiras[i] = None
                    return True                     
    
    def getIds(self):
        return [name.getId() for name in self.cadeiras if name != None]


