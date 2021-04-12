from passageiro import *

class Topic:
    numeroTotalDePassageiros = 0
    def __init__(self, lotacao, preferencial):
        self.cadeiras = [None for _ in range(lotacao)]
        self.lotacao = lotacao
        self.preferencial = preferencial

    def show(self):
        string = '[ '
        for i in range(0, self.preferencial):
            if self.cadeiras[i] != None:
                string += '@' + str(self.cadeiras[i]) 
            else:
                string += '   @   '
        for i in range(self.preferencial,  self.lotacao):
            if self.cadeiras[i] != None:
                string += '=' + str(self.cadeiras[i]) 
            else:
                string += '   =   '
        return string + ' ]'
    
    def gerenciaEntradas(self, nome, idade):
        if nome in self.getIds():
            return "fail: usuário já cadastrado"

        if idade < 50:
            if self.inserirVagasNormais(nome, idade):
                return "sucesso"
            elif self.inserirVagasPreferenciais(nome, idade):
                return "sucesso"
            return "Lotado"
        elif idade > 50: 
            if self.inserirVagasPreferenciais(nome, idade):
                return "sucesso"
            elif self.inserirVagasNormais(nome, idade):
                return "sucesso"
            return "Lotado"
    
    def inserirVagasNormais(self, nome, idade):
        for i in range(self.preferencial, self.lotacao):
            if self.cadeiras[i] == None:
                self.cadeiras[i] = Passageiro(nome, idade)
                Topic.numeroTotalDePassageiros += 1
                return True
        return False

    def inserirVagasPreferenciais(self, nome, idade):
        for i in range(0, self.preferencial):
            if self.cadeiras[i] == None:
                self.cadeiras[i] = Passageiro(nome, idade)
                Topic.numeroTotalDePassageiros += 1
                return True
        return False

    def getIds(self):
        return [passageiro.getId() for passageiro in self.cadeiras if passageiro != None ]

    def out(self, nome):
        if nome in self.getIds():
            for i in range(0, self.lotacao):
                if self.cadeiras[i].getId() == nome:
                    self.cadeiras[i] = None
                    Topic.numeroTotalDePassageiros -= 1
                    return 'Sucesso: usuário {}'.format(nome) + " removido"
        return 'fail: usuário não existe'

