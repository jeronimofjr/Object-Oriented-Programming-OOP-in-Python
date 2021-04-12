class Espiral:
    def __init__(self, nome='Empty', qtd=0, preco=0.0):
        self.nome = nome
        self.qtd = qtd
        self.preco = preco

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getQtd(self):
        return self.qtd
    
    def setQtd(self, qtd=0):
        self.qtd = self.getQtd() + qtd

    def getPreco(self):
        return self.preco
    
    def setPreco(self, preco):
        self.preco = preco
    
    def toString(self):
        return ' [ ' + self.getNome() + ' : ' + str(self.getQtd()) + ' U' + ' : ' + str(self.getPreco()) + ' $]'
