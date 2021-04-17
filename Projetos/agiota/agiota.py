from historico import *
from cliente import *

class Agiota:
    def __init__(self, dinheiro=0.0):
        self.saldo = dinheiro
        self.clientes = {}
        self.historico = []
    
    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, valor):
        self.saldo = self.getSaldo() + valor

    def addCli(self, clienteId, nome):
        if clienteId in self.getClientes():
            return 'Fail: cliente já inserido'

        cliente = Cliente(clienteId, nome)
        self.clientes.update({clienteId : cliente})
        
        return 'Sucess: cliente inserido'
    
    def emprestar(self, clienteId, valor):
        if clienteId not in self.getClientes():
            return 'Fail: cliente não existe'

        if valor > self.getSaldo():
            return 'Fail: saldo insuficiente'
        
        self.setSaldo(-valor)
        self.clientes[clienteId].setSaldo(valor)
        self.historico.append(Historico(clienteId, -valor))
        return 'Sucess: dinheiro emprestado'
    
    def receber(self, clienteId, valor):
        if clienteId not in self.getClientes():
            return 'Fail: cliente não existe'

        if valor > self.clientes[clienteId].getSaldo():
            return 'Fail: valor maior que a divida'
        
        self.setSaldo(valor)
        self.clientes[clienteId].setSaldo(-valor)
        self.historico.append(Historico(clienteId, valor))
        
        return 'Sucess: dinheiro pago'

    def matar(self, clienteId):
        del self.clientes[clienteId]
        
        for i in range(len(self.historico)):
            if self.historico[i].getId() == clienteId:
                del self.historico[i]

    def filtrar(self, nome):
        return '\n'.join([i.toString() for i in self.historico if i.getNome() == nome]) + '\nSaldo {}: {}'.format(nome, -self.clientes[nome].getSaldo())
    
    def matar(self, nome):
        self.clientes.pop(nome, None)

    def __str__(self):
        return 'Lista de clientes\n' + '\n'.join(self.getClientes())
    
    def getClientes(self):
        return  [key for key in self.clientes]

    def resumo(self):  
        return '\n'.join([self.clientes[key].toString() for key in self.clientes]) + '\nSaldo: ' + str(self.saldo)
        # adicionar saldo do agiota 

    def historicoClientes(self):
        return '\n'.join([transacao.toString() for transacao in self.historico])