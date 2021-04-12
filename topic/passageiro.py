class Passageiro:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
    
    def getId(self):
        return self.name

    def getIdade(self):
        return self.idade
    
    def __str__(self):
        return self.name + ":" + str(self.idade) + " "