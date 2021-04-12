from fone import *

class Contato:
    def __init__(self, nome="Vazio"):
        self.nome = nome
        self.fones = []

    def getNome(self):
        return self.nome

    def getFones(self):
        return ''.join('[' + str(pos) + ':' + self.fones[pos].toString() + ']' for pos in range(0, len(self.fones)))  
    
    def __str__(self):
        return self.getNome() + "=> " + self.getFones()

    def addFone(self, Fone):
        if Fone.validate():
            self.fones.append(Fone)
            return 'Sucesso: contato adicionado'
        return "Fail: numero invalido"

    def rmFone(self, indice):
        if self.fones:
            self.fones.pop(indice)
            return 'Sucesso: número apagado com'
        return 'Fail: Vc não possue números'
