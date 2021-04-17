class Historico:
    total = 0
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.id = Historico.total
        Historico.total += 1
    
    def getNome(self):
        return self.nome
    
    def getValor(self):
        return self.valor
    
    def getId(self):
        return self.id
    
    def toString(self):
        return 'id:' + str(self.getId()) + ' [' + self.getNome() + ' ' + str(self.getValor()) + ']'