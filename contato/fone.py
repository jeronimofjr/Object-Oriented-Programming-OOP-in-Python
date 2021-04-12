import re
from contato import *

class Fone:
    def __init__(self,label, numero):
        self.label = label
        self.numero = numero

    def getLabel(self):
        return self.label
    
    def getNumero(self):
        return self.numero

    def validate(self):
        padrao = r"\d{2}\-\d{2}"
        return bool(re.match(padrao, self.getNumero()))

    def toString(self):
        return self.getLabel() + ':' + self.getNumero()