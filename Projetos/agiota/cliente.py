class Cliente:
    def __init__(self, clienteId, nome, saldo=0.0):
        self.id = clienteId
        self.nome = nome
        self.saldo = saldo

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome  

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, valor):
        self.saldo = self.getSaldo() + valor 

    def toString(self):
        return self.getId() + ' : ' + self.getNome() + ' : ' + str(self.getSaldo())