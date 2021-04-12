from espiral import *

class Machine:
    
    def __init__(self, numeroDeEspirais, maxProdutos):
        self.numeroDeEspirais = numeroDeEspirais
        self.maxProdutos = maxProdutos
        self.espirais = [ Espiral()  for _ in range(numeroDeEspirais)]
        self.saldo = 0.0

    def getMaxProdutos(self):
        return self.maxProdutos

    def getNumeroDeEspirais(self):
        return self.numeroDeEspirais

    def getSaldo(self):
        return self.saldo
    
    def setSaldo(self, valor):
        self.saldo = self.getSaldo() + valor

    def limpar(self, indice):
        self.espirais[indice] = Espiral()

    def setC(self, indice, food, qtd, preco):
        if qtd + self.espirais[indice].getQtd() > self.getMaxProdutos():
            return 'Fail: quantidade excedida'
        self.espirais[indice].setNome(food)
        self.espirais[indice].setPreco(preco)
        self.espirais[indice].setQtd(qtd)
        return 'Sucesso'

    def vender(self, indice):
        if self.espirais[indice].getQtd() > 0:
            if self.espirais[indice].getPreco() > self.getSaldo():
                return "Saldo insuficiente"
            self.espirais[indice].setQtd(-1)
            self.setSaldo(-self.espirais[indice].getPreco())
            return "Voce comprou um " + self.espirais[indice].getNome()
        return "Não tem no estoque"

    def gerenciarCompraEAlocacao(self, indice):
        if indice > self.getNumeroDeEspirais():
            return True
        
    def dinheiroVai(self, valor):
        self.setSaldo(valor)
    
    def pedirTroco(self):
        troco = self.getSaldo()
        self.setSaldo(-troco)
        return troco

    def toString(self):
        return  "Saldo: " + str(self.getSaldo()) + '\n' + '\n'.join([ str(i) + self.espirais[i].toString()  for i in range(0,self.getNumeroDeEspirais())]) 
